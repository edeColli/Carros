import openai


def get_car_ai_bio(model, brand, year):
    prompt = ''''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    '''    
    openai.api_key = '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'
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000
    )
    return response['choices'][0]['text']