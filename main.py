import flet as ft


def main(page: ft.Page):
    
    def button_clicked(e):
        task_view.controls.append(ft.Checkbox(label = new_task.value))
        new_task.value = ''
        # 特定のWidgetにのみ変更を加えられることができる
        main_view.update()
        
    new_task = ft.TextField(hint_text = 'やるべきこと', expand = True)
    add_task_button = ft.ElevatedButton(text = '追加', icon = 'add',on_click = button_clicked)
    task_view = ft.Column()
    main_view = ft.Column(
        controls = [
            ft.Row(
                controls = [
                    new_task,
                    add_task_button
                ]
            ),
            task_view
        ]
    )
    page.add(main_view)
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

ft.app(target=main)