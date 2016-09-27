import re

from scrapy.spiders import Spider
from scrapy.selector import Selector

#---------------------------------------------------#
class ProblemsSpider(Spider):
    name = "problems"

    allowed_domains = ["urionlinejudge.com.br"]
    problems_array = []

    custom_settings = {
        'DOWNLOAD_HANDLERS' : {'s3': None,}
    }

    def __init__(self, *args, **kwargs):
        super(ProblemsSpider, self).__init__(*args, **kwargs)
        AWS_ACCESS_KEY_ID = ""
        AWS_SECRET_ACCESS_KEY = ""
        self.start_urls = kwargs.get('urls')

    def parse(self, response):
        sel = Selector(response)
        
        numero = response.url
        start = "https://www.urionlinejudge.com.br/repository/UOJ_"
        end = ".html"
        numero = re.findall(r'{0}(.*?){1}'.format(start, end), numero)[0]
        
        titulo_path = sel.xpath('//*[@class="header"]/h1/text()')
        titulo = titulo_path.extract()[0]
        titulo = titulo.strip()
       
        descricao_path = sel.xpath('string(//*[@class="description"])')
        descricao = descricao_path.extract()[0]
        descricao = re.sub(' +', ' ', descricao)
        descricao = re.sub('<.*?>', '', descricao)
        descricao = re.sub('\s+', ' ', descricao)
        descricao = descricao.strip()

        entrada_path = sel.xpath('string(//*[@class="input"])')
        entrada = entrada_path.extract()[0]
        entrada = re.sub(' +', ' ', entrada)
        entrada = re.sub('<.*?>', '', entrada)
        entrada = re.sub('\s+', ' ', entrada)
        entrada = entrada.strip()

        saida_path = sel.xpath('string(//*[@class="output"])')
        saida = saida_path.extract()[0]
        saida = re.sub(' +', ' ', saida)
        saida = re.sub('<.*?>', '', saida)
        saida = re.sub('\s+', ' ', saida)
        saida = saida.strip()
 

        item = {
            'numero': numero,
            'titulo': titulo,
            'descricao': descricao,
            'entrada': entrada,
            'saida': saida,
            'assunto': '',
            'nivel': ''
        }

        self.problems_array.append(item)
        return item
#---------------------------------------------------#
