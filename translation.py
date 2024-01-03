import pandas as pd

# Словарь перевода признаков
header_translation_dict = {
    'cap-shape': 'форма шляпки',
    'cap-surface': 'поверхность шляпки',
    'cap-color': 'цвет шляпки',
    'bruises': 'повреждения',
    'odor': 'запах',
    'gill-attachment': 'крепление пластинок',
    'gill-spacing': 'расстояние между пластинками',
    'gill-size': 'размер пластинок',
    'gill-color': 'цвет пластинок',
    'stalk-shape': 'форма ножки',
    'stalk-root': 'корень ножки',
    'stalk-surface-above-ring': 'поверхность ножки выше кольца',
    'stalk-surface-below-ring': 'поверхность ножки ниже кольца',
    'stalk-color-above-ring': 'цвет ножки выше кольца',
    'stalk-color-below-ring': 'цвет ножки ниже кольца',
    'veil-type': 'тип вуали',
    'veil-color': 'цвет вуали',
    'ring-number': 'количество колец',
    'ring-type': 'тип кольца',
    'spore-print-color': 'цвет спор',
    'population': 'популяция',
    'habitat': 'среда обитания',
    'edible': 'съедобность'
}

# Словарь перевода значений признаков
feature_translation_dict = {
    'форма шляпки': {'b': 'колокольчатая', 'c': 'коническая', 'x': 'выпуклая', 'f': 'плоская', 'k': 'кнопочная',
                     's': 'втопленная'},
    'поверхность шляпки': {'f': 'волокнистая', 'g': 'желобковатая', 'y': 'чешуйчатая', 's': 'гладкая'},
    'цвет шляпки': {'n': 'коричневая', 'b': 'бежевая', 'c': 'бурая', 'g': 'серая', 'r': 'зеленая', 'p': 'розовая',
                    'u': 'фиолетовая', 'e': 'красная', 'w': 'белая', 'y': 'желтая'},
    'повреждения': {'t': 'переломы', 'f': 'нет'},
    'запах': {'a': 'миндальный', 'l': 'анисовый', 'c': 'смолистый', 'y': 'рыбный', 'f': 'тухлый', 'm': 'затхлый',
              'n': 'нет', 'p': 'жгучий', 's': 'пряный'},
    'крепление пластинок': {'a': 'прикрепленные', 'd': 'опущенные', 'f': 'свободные', 'n': 'выемчатые'},
    'расстояние между пластинками': {'c': 'близкие', 'w': 'плотные', 'd': 'далекие'},
    'размер пластинок': {'b': 'широкие', 'n': 'узкие'},
    'цвет пластинок': {'k': 'черные', 'n': 'коричневые', 'b': 'бежевые', 'h': 'шоколадные', 'g': 'серые',
                       'r': 'зеленые', 'o': 'оранжевые', 'p': 'розовые', 'u': 'фиолетовые', 'e': 'красные',
                       'w': 'белые', 'y': 'желтые'},
    'форма ножки': {'e': 'удлиняющиеся', 't': 'сужающиеся'},
    'корень ножки': {'b': 'луковичная', 'c': 'клубневая', 'u': 'чашечная', 'e': 'равномерная', 'z': 'ризоморфы',
                     'r': 'корневая', '?': 'отсутствует'},
    'поверхность ножки выше кольца': {'f': 'волокнистая', 'y': 'чешуйчатая', 'k': 'шелковистая', 's': 'гладкая'},
    'поверхность ножки ниже кольца': {'f': 'волокнистая', 'y': 'чешуйчатая', 'k': 'шелковистая', 's': 'гладкая'},
    'цвет ножки выше кольца': {'n': 'коричневый', 'b': 'бежевый', 'c': 'коричнево-красный', 'g': 'серый',
                               'o': 'оранжевый', 'p': 'розовый', 'e': 'красный', 'w': 'белый', 'y': 'желтый'},
    'цвет ножки ниже кольца': {'n': 'коричневый', 'b': 'бежевый', 'c': 'коричнево-красный', 'g': 'серый',
                               'o': 'оранжевый', 'p': 'розовый', 'e': 'красный', 'w': 'белый', 'y': 'желтый'},
    'тип вуали': {'p': 'частичная', 'u': 'универсальная'},
    'цвет вуали': {'n': 'коричневый', 'o': 'оранжевый', 'w': 'белый', 'y': 'желтый'},
    'количество колец': {'n': 'нет', 'o': 'одно', 't': 'два'},
    'тип кольца': {'c': 'паутинчатое', 'e': 'исчезающее', 'f': 'расширяющееся', 'l': 'крупное', 'n': 'нет',
                   'p': 'подвесное', 's': 'защитное', 'z': 'зонированное'},
    'цвет спор': {'k': 'черный', 'n': 'коричневый', 'b': 'бежевый', 'h': 'шоколадный', 'r': 'зеленый', 'o': 'оранжевый',
                  'u': 'фиолетовый', 'w': 'белый', 'y': 'желтый'},
    'популяция': {'a': 'многочисленное', 'c': 'скопленное', 'n': 'многочисленное', 's': 'рассеянное', 'v': 'несколько',
                  'y': 'одиночное'},
    'среда обитания': {'g': 'травы', 'l': 'листва', 'm': 'луга', 'p': 'тропинки', 'u': 'городская', 'w': 'загрязненная',
                       'd': 'леса'},
    'съедобность': {'p': 'ядовит', 'e': 'съедобен'}
}


def translate_dataset(file_path):
    # Чтение CSV файла
    df = pd.read_csv(file_path)

    # Перевод данных
    df.columns = df.columns.map(header_translation_dict)
    df.replace(feature_translation_dict, inplace=True)

    # Запись обновленных данных в CSV файл
    df.to_csv('data/mushroom_dataset_ru.csv', index=False, encoding='utf-8')