import flet as ft
import requests


class Shop(ft.UserControl):
    def __init__(self, shop_name, shop_image, shop_address, shop_genre, shop_budget):
        super().__init__()
        self.shop_name = shop_name
        self.shop_image = shop_image
        self.shop_address = shop_address
        self.shop_genre = shop_genre
        self.shop_budget = shop_budget

    def build(self):

        self.shop_card = ft.Card(
            content=ft.Container(
                height=100,
                padding=10,
                content=ft.Row(
                    [
                        ft.Image(
                            src=self.shop_image,
                            width=200,
                            height=200,
                            fit=ft.ImageFit.NONE,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Column(
                            [
                                ft.Row([ft.Text('ジャンル: '), ft.Text(
                                    value=self.shop_genre),]),
                                ft.Row([ft.Text('店名: '), ft.Text(
                                    value=self.shop_name),]),
                                ft.Row([ft.Text('予算: '), ft.Text(
                                    value=self.shop_budget),]),

                            ]
                        )
                    ]
                ),
            )
        )

        return self.shop_card


class TodoApp(ft.UserControl):
    def build(self):
        self.place_name = ft.TextField(hint_text='飲食店を知りたい地域', expand=True)
        self.search_weather_button = ft.ElevatedButton(
            text='検索', icon='search', on_click=self.search_clicked)
        self.shop_list = ft.ListView(expand=True, spacing=10)
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.place_name,
                        self.search_weather_button
                    ]
                ),
                ft.Container(
                    content=self.shop_list,
                    height=600
                )
            ]
        )

    def search_clicked(self, e):
        self.shop_list.controls = []
        place = self.place_name.value
        api_key = '7b8368a0d26c03a1'
        url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
        body = {
            'key': api_key,
            'keyword': place,
            'format': 'json',
            'count': 15
        }
        response = requests.get(url, body)
        datum = response.json()
        stores = datum['results']['shop']
        for store in stores:
            name = store['name']

            image = store['logo_image']

            address = store['address']

            genre = store['genre']['name']

            budget = store['budget']['name']

            shop = Shop(shop_name=name, shop_image=image,
                        shop_address=address, shop_genre=genre, shop_budget=budget,)

            self.shop_list.controls.append(shop)
        self.update()


def main(page: ft.Page):
    page.title = '飲食店検索アプリ'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    todo = TodoApp()

    page.add(todo)


ft.app(target=main)