import flet as ft

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text = 'やるべきこと', expand = True)
        self.add_task_button = ft.ElevatedButton(text = '追加', icon = 'add',on_click = self.button_clicked)
        self.task_view = ft.Column()
        
        return ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        self.new_task,
                        self.add_task_button
                    ]
                ),
                self.task_view
            ]
        )
        
    
    def button_clicked(self, e):
        self.task_view.controls.append(ft.Checkbox(label = self.new_task.value))
        self.new_task.value = ''
        # 特定のWidgetにのみ変更を加えられることができる
        self.update()
        
        

def main(page: ft.Page):
    page.title = 'Todoアプリ'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    todo  = TodoApp()
    
    page.add(todo)
    

ft.app(target=main)