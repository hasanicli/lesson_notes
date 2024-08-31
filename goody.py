def sort_list_turkish(names, reverse=False):
    letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
    letters_dict = {letter: letters.index(letter) for letter in letters}
    names.sort(key=lambda x: letters_dict[x[0]], reverse=reverse)
    return names


def sort_dict_turkish_by_key(item_dict, reverse=False):
    letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
    letters_dict = {letter: letters.index(letter) for letter in letters}
    return dict(sorted(item_dict.items(), key=lambda x: letters_dict[x[0][0]], reverse=reverse))


def sort_dict_turkish_by_key_2(item_dict, reverse=False):
    letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
    letters_dict = {letter: letters.index(letter) for letter in letters}
    return {k: v for k, v in sorted(item_dict.items(), key=lambda x: letters_dict[x[0][0]], reverse=reverse)}


def sort_dict_turkish_by_value(item_dict, reverse=False):
    letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
    letters_dict = {letter: letters.index(letter) for letter in letters}
    return dict(sorted(item_dict.items(), key=lambda x: letters_dict[x[1][0]], reverse=reverse))


def sort_dict_turkish_by_value_2(item_dict, reverse=False):
    letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
    letters_dict = {letter: letters.index(letter) for letter in letters}
    return {k: v for k, v in sorted(item_dict.items(), key=lambda x: letters_dict[x[1][0]], reverse=reverse)}


def sort_by_value_1(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def sort_by_value_2(x):
    return dict(sorted(x.items(), key=lambda item: item[1]))


def sort_by_key_1(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}


def sort_by_key_2(x):
    return dict(sorted(x.items(), key=lambda item: item[0]))


if __name__ == '__main__':
    x_dict = {"Hasan": "İçli", "Metin": "Aydın", "Kemal": "Sunal", "Ferdi": "Tayfur", "Zülfü":"Livaneli", "İbrahim": "Tatlıses", "Şule": "İçli", "Çiğdem": "Talu"}
    print(sort_by_key_1(x_dict))
    print(sort_dict_turkish_by_key(x_dict,False))
