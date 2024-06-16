import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader


class LiteratureTestApp(App):
    def build(self):
        self.questions = self.load_questions()
        self.score = 0
        self.index = 0
        self.create_widgets()
        self.sound_correct = SoundLoader.load('correct.mp3')
        self.sound_wrong = SoundLoader.load('wrong.mp3')
        return self.layout

    def load_questions(self):
        # Полный путь к директории с изображениями вопросов
        images_folder = './images'

        if not os.path.exists(images_folder):
            raise FileNotFoundError(f"Директория '{images_folder}' не существует.")

        questions = []
        for i in range(1, 11):  # 10 вопросов с номерами от 1 до 10
            image_path = os.path.join(images_folder, f'{i}.jpg')
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Изображение '{image_path}' не найдено.")

            # Добавляем текстовое описание и правильный ответ для каждого вопроса
            if i == 1:
                question = {
                    'image': image_path,
                    'description': 'Какой писатель написал произведение "Война и мир"?',
                    'answers': ['Лев Толстой', 'Федор Достоевский', 'Иван Тургенев', 'Александр Пушкин'],
                    'correct_answer': 'Лев Толстой'
                }
            elif i == 2:
                question = {
                    'image': image_path,
                    'description': 'Какая книга Льюиса Кэрролла рассказывает о приключениях Алисы в Стране Чудес?',
                    'answers': ['Алиса в Зазеркалье', 'Алиса в Стране Чудес', 'Алиса и Кот в Сапогах', 'Алиса и Гринч'],
                    'correct_answer': 'Алиса в Стране Чудес'
                }
            elif i == 3:
                question = {
                    'image': image_path,
                    'description': 'Какой роман Ф. С. Фицджеральда описывает жизнь американской высшей сословии в 1920-е годы?',
                    'answers': ['Великий Гэтсби', 'Похождения Гекльберри Финна', 'Белый клык', 'Три товарища'],
                    'correct_answer': 'Великий Гэтсби'
                }
            elif i == 4:
                question = {
                    'image': image_path,
                    'description': 'Какой автор написал роман "Преступление и наказание"?',
                    'answers': ['Федор Достоевский', 'Лев Толстой', 'Александр Пушкин', 'Иван Тургенев'],
                    'correct_answer': 'Федор Достоевский'
                }
            elif i == 5:
                question = {
                    'image': image_path,
                    'description': 'Какая книга Дж. Р. Р. Толкина рассказывает о приключениях Фродо Бэггинса?',
                    'answers': ['Властелин колец', 'Хоббит, или Туда и обратно', 'Сильмариллион', 'Некромант'],
                    'correct_answer': 'Властелин колец'
                }
            elif i == 6:
                question = {
                    'image': image_path,
                    'description': 'Какое произведение Александра Пушкина считается его важнейшим стихотворением?',
                    'answers': ['Евгений Онегин', 'Медный всадник', 'Дубровский', 'Руслан и Людмила'],
                    'correct_answer': 'Евгений Онегин'
                }
            elif i == 7:
                question = {
                    'image': image_path,
                    'description': 'Какой писатель написал произведение "1984"?',
                    'answers': ['Джордж Оруэлл', 'Альдоус Хаксли', 'Рэй Брэдбери', 'Исаак Азимов'],
                    'correct_answer': 'Джордж Оруэлл'
                }
            elif i == 8:
                question = {
                    'image': image_path,
                    'description': 'Какой роман Эрнеста Хемингуэя рассказывает о враче-алкоголике, ищущем смысл жизни в мексиканских джунглях?',
                    'answers': ['Старик и море', 'По ком звонит колокол', 'Прощай, оружие!', 'На дороге'],
                    'correct_answer': 'На дороге'
                }
            elif i == 9:
                question = {
                    'image': image_path,
                    'description': 'Кто написал роман "Мастер и Маргарита"?',
                    'answers': ['Михаил Булгаков', 'Анна Ахматова', 'Борис Пастернак', 'Иван Бунин'],
                    'correct_answer': 'Михаил Булгаков'
                }
            elif i == 10:
                question = {
                    'image': image_path,
                    'description': 'Какой роман Джейн Остин рассказывает о сложностях выбора супруга для героини?',
                    'answers': ['Гордость и предубеждение', 'Эмма', 'Смешные ученья', 'Разум и чувства'],
                    'correct_answer': 'Гордость и предубеждение'
                }


            questions.append(question)

        random.shuffle(questions)  # случайное перемешивание вопросов
        return questions

    def create_widgets(self):
        self.layout = BoxLayout(orientation='vertical')

        # Виджет для изображения вопроса
        self.question_image = Image(source=self.questions[self.index]['image'])
        self.layout.add_widget(self.question_image)

        # Виджет для текстового описания вопроса
        self.question_description = Label(text=self.questions[self.index]['description'], size_hint=(1, None), height=50)
        self.layout.add_widget(self.question_description)

        # Создаем виджеты ответов для текущего вопроса
        self.answers_layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.answers_layout)
        self.create_answer_buttons()

    def create_answer_buttons(self):
        # Очищаем текущие кнопки ответов
        self.answers_layout.clear_widgets()

        # Создаем новые кнопки ответов для текущего вопроса
        answers = self.questions[self.index]['answers']
        random.shuffle(answers)
        for answer in answers:
            button = Button(text=answer, size_hint=(None, None), size=(400, 50))
            button.bind(on_release=self.check_answer)
            self.answers_layout.add_widget(button)

    def check_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.questions[self.index]['correct_answer']

        if selected_answer == correct_answer:
            self.score += 1
            self.sound_correct.play()
        else:
            self.sound_wrong.play()

        self.index += 1

        if self.index < len(self.questions):
            # Переходим к следующему вопросу
            self.question_image.source = self.questions[self.index]['image']
            self.question_description.text = self.questions[self.index]['description']
            self.create_answer_buttons()  # создаем заново кнопки ответов для нового вопроса
        else:
            # Выводим результаты теста
            self.show_results()

    def show_results(self):
        score_label = Label(text=f'Вы набрали {self.score} из {len(self.questions)} баллов.')
        close_button = Button(text='Закрыть', size_hint=(None, None), size=(200, 50))
        close_button.bind(on_release=self.close_app)

        box = BoxLayout(orientation='vertical')
        box.add_widget(score_label)
        box.add_widget(close_button)

        popup = Popup(title='Результаты теста', content=box, size_hint=(None, None), size=(400, 200))
        popup.open()

    def close_app(self, instance):
        self.stop()


if __name__ == '__main__':
    LiteratureTestApp().run()
