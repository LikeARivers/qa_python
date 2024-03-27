import pytest
from main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_dont_set_book_with_new_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Фрида Кало')
        collector.set_book_genre('Фрида Кало', 'Автобиография')
        assert not collector.get_book_genre('Фрида Кало') == 'Автобиография'

    @pytest.mark.parametrize("name, genre", [("Шерлок Холмс", "Детективы"), ("12 стульев", "Комедии")])
    def test_get_book_genre_get_two_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Агата Кристи')
        collector.set_book_genre('Агата Кристи', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс', 'Агата Кристи']

    def test_get_books_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        assert collector.get_books_genre() == {'Шерлок Холмс': 'Детективы', 'Незнайка': 'Мультфильмы'}

    def test_get_books_for_children_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Незнайка')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.set_book_genre('12 стульев', 'Комедии')
        assert collector.get_books_for_children() == ['Незнайка', '12 стульев']

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_get_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']
