import flet as ft

#TODO DleteメソッドをTaskクラスに渡す理由

# UserControlとは？
class Task(ft.UserControl):
    def __init__(self, task_name, delte_task):
        super().__init__()
        self.task_name = task_name
        self.delte_task = delte_task
    def build(self):
        self.display_task = ft.Checkbox(label = self.task_name)
        self.edit_task_name = ft.TextField()
        
        # 通常表示
        self.default_task_view = ft.Row(
            controls= [
                self.display_task,
                ft.Row(
                    controls = [
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="タスクを編集",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon = ft.icons.DELETE_OUTLINE,
                            tooltip = "タスクを削除",
                            on_click = self.delete_clicked,
                        ),
                    ]
                ),
            ]
        )
        
        
        # 編集ボタンが押された時（普段は隠しておく）
        self.edit_task_view = ft.Row(
            visible=False,
            controls=[
                self.edit_task_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="タスク更新",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.default_task_view, self.edit_task_view])
    
    # TODO 引数eは何を意味しているのか？
    def edit_clicked(self, e):
        self.default_task_view.visible = False
        self.edit_task_view.visible = True
        self.edit_task_name.value = self.task_name
        
        self.update()
    
    def delete_clicked(self, e):
        self.delte_task(self)
        
    def save_clicked(self, e):
        self.display_task.label = self.edit_task_name.value
        self.default_task_view.visible = True
        self.edit_task_view.visible = False
        
        self.update()

class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text = 'やるべきこと', expand = True)
        self.add_task_button = ft.ElevatedButton(text = '追加', icon = 'add',on_click = self.add_clicked)
        self.tasks = ft.Column()
        
        return ft.Column(
            controls = [
                ft.Row(
                    controls = [
                        self.new_task,
                        self.add_task_button
                    ]
                ),
                self.tasks
            ]
        )
        
    def delete_task(self, task):
        self.tasks.controls.remove(task)
        self.update()
    
    def add_clicked(self, e):
        self.task = Task(task_name=self.new_task.value, delte_task=self.delete_task)
        self.tasks.controls.append(self.task)
        self.new_task.value = ''
        # 特定のWidgetにのみ変更を加えられることができる
        self.update()
        
        

def main(page: ft.Page):
    page.title = 'Todoアプリ'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    todo  = TodoApp()
    
    page.add(todo)
    

ft.app(target=main)