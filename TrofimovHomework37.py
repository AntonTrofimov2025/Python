"1. Класс Student"
"""Создайте класс Student, представляющий ученика.
● При создании указываются имя и email.
● Добавьте строковое представление студента (например, только имя).
● Добавьте метод notify(message), который выводит сообщение: Email to <email>: <message>
Проверьте создание объекта и вызов метода.
"""

class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    def __str__(self):
        return f"Student: {self.name}"
    def notify(self, message: str):
        print(f"Email to {self.email}: {message}")

my_student = Student("Tony", "tony2005@msn.com")
print(my_student)
my_student.notify("What's up? :)")

"""2. Класс Course
Создайте класс Course, представляющий учебный курс.
● При создании указывается название курса.
● У каждого объекта Course должно быть поле students, в котором хранится список
зарегистрированных студентов.
● Добавьте метод add_student(student), который принимает объект Student и добавляет его в курс.
● Добавьте метод show_students(), который выводит список имён студентов.
● Добавьте метод notify_all(message), который уведомляет всех студентов курса.
Проверьте работу методов, создав курс, добавив студентов и отправив уведомление.

Пример вывода:
Students enrolled in Python OOP:
- Alice
- Bob
Email to alice@example.com: Welcome to the course!
Email to bob@example.com: Welcome to the course!"""

class Course:
    def __init__(self, your_course: str):
        self.your_course = your_course
        self.students = []
    def add_student(self, student: Student):
        self.students.append(student)
    def show_students(self):
        print(f"Students enrolled in {self.your_course}:\n{'\n'.join(f'- {student.name}' for student in self.students)}")
    def notify_all(self, message):
        for student in self.students:
            student.notify(message)

my_student2 = Student("Alice", "alice@example.com")
my_student3 = Student("Bob", "bob@example.com")
my_course = Course("Python OOP")
my_course.add_student(my_student)
my_course.add_student(my_student2)
my_course.add_student(my_student3)
my_course.show_students()
my_course.notify_all("Welcome to the course!")
print()

"""1. Воспроизведение мультимедиа
Создайте два класса:
Класс 1
AudioFileMixin — требует наличие поля
audio_tracks (список треков).
Метод play_audio() выводит:
Воспроизведение аудио для <НазваниеКласса>:
<название трека>
<название трека>
Класс 2
VideoFileMixin — требует наличие поля
video_files (список видео).
Метод play_video() выводит:
Воспроизведение видео для <НазваниеКласса>:
<название видео>
<название видео>
Если нужное поле отсутствует — выбрасывайте AttributeError."""

class AudioFileMixin:
    def play_audio(self):
        if not (hasattr(self, "audio_tracks") and isinstance(self.audio_tracks, list)):
            raise AttributeError("Field audio_tracks is missing or not a list!!")
        if not all(isinstance(track, str) for track in self.audio_tracks):
            raise TypeError("All list elements should be str!!")
        return "\n".join(self.audio_tracks)

class VideoFileMixin:
    def play_video(self):
        if not (hasattr(self, "video_files") and isinstance(self.video_files, list)):
            raise AttributeError("Field video_files is missing or not a list!!")
        if not all(isinstance(video, str) for video in self.video_files):
            raise TypeError("All list elements should be str!!")
        return "\n".join(self.video_files)

# class VideoBank(VideoFileMixin):
#     def __init__(self):
#         self.video_files = []
#     def add_video(self, your_video: str):
#         self.video_files.append(your_video)
#
# my_vid_bank = VideoBank()
# my_vid_bank.add_video("Video_Cats")
# my_vid_bank.add_video("Video_Dogs")
# my_vid_bank.add_video("Video_Vacations")
#
# try:
#     print(my_vid_bank.play_video())
# except (TypeError, AttributeError) as e:
#     print(e)
# print()
#
# class AudioGuide(AudioFileMixin):
#     def __init__(self):
#         self.audio_tracks = []
#     def add_your_favorite_track(self, your_track: str):
#         self.audio_tracks.append(your_track)
#
# my_audios = AudioGuide()
# my_audios.add_your_favorite_track("Britney Spears Toxic")
# my_audios.add_your_favorite_track("Bon Jovi It's My Life")
# my_audios.add_your_favorite_track("Linkin Park Breaking the Habit")
#
# try:
#     print(my_audios.play_audio())
# except (TypeError, AttributeError) as e:
#     print(e)
# print()

"""2. Устройства
Создайте два класса:
● MediaPlayer — поддерживает только аудио. Принимает список треков.
● Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения."""

class MediaPlayer(AudioFileMixin):
    def __init__(self, your_track_list: list[str]):
        self.audio_tracks = your_track_list
        # for track in self.your_track_list:
        #     self.audio_tracks.append(track)


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, your_audio_list: list[str], your_vid_list: list[str]):
        self.audio_tracks = your_audio_list
        self.video_files = your_vid_list
        # for audio in self.your_audio_list:
        #     self.audio_tracks.append(audio)
        # for video in self.your_vid_list:
        #     self.video_files.append(video)

my_tracks = ["Britney Spears Toxic", "Bon Jovi It's My Life", "Linkin Park Breaking the Habit"]
my_vids = ["Video_Cats", "Video_Dogs", "Video_Vacations"]

my_laptop = Laptop(my_tracks, my_vids)
my_media_player = MediaPlayer(my_tracks)

laptop_audio = my_laptop.play_audio()
laptop_video = my_laptop.play_video()
media_player_audio = my_media_player.play_audio()

print(f"Воспроизведение аудио для {my_laptop.__class__.__name__}:\n{laptop_audio
        if laptop_audio else '- No Audio Found'}")
print(f"Воспроизведение видео для {my_laptop.__class__.__name__}:\n{laptop_video
        if laptop_video else '- No Video Found'}")
print()
print(f"Воспроизведение аудио для {my_media_player.__class__.__name__}:\n{media_player_audio
        if media_player_audio else '- No Audio Found'}")