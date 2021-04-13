import wikipedia

wikipedia.set_lang("ru")


def search_wiki(word):
    print(word)
    try:
        if word:
            w2 = wikipedia.page(word).url
            w1 = wikipedia.summary(word)
            return w1, "\nСсылка: " + w2
        return "Запрос в виикипедии не найден", ""
    except:
        return "Запрос в виикипедии не найден", ""
