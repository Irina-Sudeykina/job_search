# Проект "job_search" - Поиск вакансий

## Описание:
 Проект "job_search" - это проект на Python, 
 осуществляющий поиск вакансий на hh.ru
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/job_search.git
 
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
  
 ### Класс **BaseProduct**
 Абстрактный класс, родительский для класса Product.
 Имеет абстрактный метод new_product, 
 который необходимо переопределять для каждого потомка.

 #### Пример использования: 
 ```
from src.product import Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)
print(new_product.name)
print(new_product.description)
print(new_product.price)
print(new_product.quantity)

 ```
 #### Пример работы:
 ```
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5

Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
10
 ```



 ## Тестирование:
Проект покрыт тестами фреймворка pytest. Для их запуска выполните команду:
```
pytest
```
Для выгрузки отчета о покрытии проекта тестами выполните команду:
```
pytest --cov=src --cov-report=html
```


 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 