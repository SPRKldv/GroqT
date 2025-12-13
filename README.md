# GroqT

Минималистичный терминальный клиент для работы с **Groq API**.

![console](scr.jpg)
## Возможности
- Общение с Groq прямо из **консоли**
- Цветной вывод ответов (скоро)
- Поддержка разных моделей (просто изменив модель если хотите)
- Чистый и понятный код

## Установка
```
git clone https://github.com/SPRKldv/GroqT.git
 cd GroqT
pip install groq rgbprint
```

## Настройка

Вставь свой **API-ключ** в коде, взять тут — groq.com:

```
api = "YOUR_GROQ_API_KEY"
```

**Модель** изменить можно в данном разделе:

```
model = "openai/gpt-oss-120b"
```

## Запуск

```
python main.py
```

**Для выхода:**

```
exit или CTRL + C
```
