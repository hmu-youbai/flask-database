from demo import create_app
from demo.blueprint.search import db, Gene
import csv

app = create_app()  # 确保这个函数返回配置好的 Flask 应用实例



def import_genes(filename):
    with app.app_context():  # 这确保了在 Flask 应用上下文中运行
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # 跳过头部
            for row in reader:
                if len:
                    symbol, ensembl = row  # 解包每行的两个列值
                    if symbol=="" or ensembl =="":
                        continue
                    gene = Gene(symbol=symbol, ensembl=ensembl)
                    db.session.add(gene)
            db.session.commit()  # 提交所有变更到数据库


if __name__ == '__main__':
    import_genes('genes.csv')

