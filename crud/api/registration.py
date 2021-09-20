class Villain:
    list_villains = [
        {
            'villain_id': 1,
            'nome': 'Thanos',
            'idade': 48,
            'criador': 'Jim Starlin'
        },
        {
            'villain_id': 2,
            'nome': 'Darkside',
            'idade': 51,
            'criador': 'Jack Kirby'
        },
        {
            'villain_id': 3,
            'nome': 'Coringa',
            'idade': 81,
            'criador': 'Jerry Robinson'
        },
        {
            'villain_id': 4,
            'nome': 'Hela',
            'idade': 57,
            'criador': 'Stan Lee'
        }
    ]

    @classmethod
    def cadastrar(cls, villain):
        cls.list_villains.append(villain)
        return villain
    
    @classmethod
    def listar(cls, villain_id=None):
        if villain_id:
            return next(filter(lambda x: x['villain_id'] == villain_id,cls.list_villains), {})
        return cls.list_villains

    @classmethod
    def deletar(cls, villain_id):
        cls.list_villains = list(filter(lambda x: x['villain_id'] != villain_id, cls.list_villains))
        return {'message': f'Vilão com id {villain_id} foi deletado com sucesso!'}

    @classmethod
    def atualizar(cls, villain_id, new_villain:dict):
        villain = next(filter(lambda x: x['villain_id'] == villain_id,cls.list_villains),{})
        index = cls.list_villains.index(villain)

        if new_villain.get('nome'):
            villain['nome'] = new_villain.get('nome')

        if new_villain.get('idade'):
            villain['idade'] = new_villain.get('idade')

        if new_villain.get('criador'):
            villain['criador'] = new_villain.get('criador')

        cls.list_villains[index] = villain
        return new_villain