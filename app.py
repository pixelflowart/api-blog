from flask import Flask, jsonify, request
from estrutura_banco_de_dados import Autor, Postagem, app, db
'''
'''
portaLocal = [5000, 7777]
#Rota padrão - GET http://localhost:5000
@app.route('/postagem/')
def obter_postagens():
    try:
        postagens = Postagem.query.all()
        lista_de_postagens = []
        for postagem in postagens:
            postagem_atual = {}
            postagem_atual['id_postagem'] = postagem.id_postagem
            postagem_atual['titulo'] = postagem.titulo
            postagem_atual['id_autor'] = postagem.id_autor
            lista_de_postagens.append(postagem_atual)
        return jsonify({'Postagem': lista_de_postagens})
    except :
        return jsonify({'Postagem': lista_de_postagens})
# GET com ID http://localhost:5000/postagem/2
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagens_por_indice(indice):
    try:
        postagem = Postagem.query.filter_by(id_postagem=indice).first()
        lista_de_postagens = []
        if not postagem:
            return jsonify({'Postagem não encontrada!'})
        postagem_atual = {}
        postagem_atual['id_postagem'] = postagem.id_postagem
        postagem_atual['titulo'] = postagem.titulo
        postagem_atual['id_autor'] = postagem.id_autor
        lista_de_postagens.append(postagem_atual)
        return jsonify({'Postagem': lista_de_postagens})
    except :
        return jsonify('Postagem não encontrada!')
# POST com ID http://localhost:5000/postagem
@app.route('/postagem/', methods=['POST'])
def nova_postagem():
    try:
        post_novo = request.get_json()
        postagem = Postagem(titulo=post_novo['titulo'], id_autor=post_novo['id_autor'])
        db.session.add(postagem)
        db.session.commit()
        return jsonify({'mensagem': 'Post criado com sucesso'}, 200)
    except :
        return jsonify({'Post não realizado!'}, 404)
# PUT com ID http://localhost:5000/postagem/2
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=indice).first()

    if not postagem:
        return jsonify({'Mensagem': 'Este usuário não foi alterado.'})
    try:
        if postagem_alterada['titulo']:
            postagem.titulo =postagem_alterada['titulo']        
    except:
        pass
    try:
        if postagem_alterada['id_autor']:
            postagem.id_autor =postagem_alterada['id_autor']
    except:
        pass

    
    db.session.commit()

    return jsonify({'Mensagem': f'Este usuário, {postagem.titulo}, foi alterado.'})
# DELETE com ID http://localhost:5000/postagem/2
@app.route('/postagem/<int:id_postagem>', methods=['DELETE'])
def deletar_postagem(id_postagem):
    postagem_a_deletar = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem_a_deletar:
        return jsonify({'Mensagem': 'Este usuário não foi deletado.'})
    db.session.delete(postagem_a_deletar)
    db.session.commit()

    return jsonify({'Mensagem': f'Este usuário, {postagem_a_deletar}, foi deletado.'})
# ROTA DE AUTOR - GET
@app.route('/autores')
def obter_aurotes():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    
    return jsonify({'autores':lista_de_autores})
# ROTA DE AUTOR - GET POR INDICE
@app.route('/autores/<int:id_autor>', methods=['GET'])
def obter_aurotes_por_id(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    lista_de_autores = []
    if not autor:
        return jsonify('Autor não encontrado.')
    
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    lista_de_autores.append(autor_atual)
    
    return jsonify({'autor':lista_de_autores})
# ROTA DE AUTOR - POST
@app.route('/autores', methods=['POST'])
def novo_autor():
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])
    db.session.add(autor)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário criado com sucesso'}, 200)
# ROTA DE AUTOR - PUT
@app.route('/autores/<int:id_autor>', methods=['PUT'])
def alterar_autor(id_autor):
    usuario_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()

    if not autor:
        return jsonify({'Mensagem': 'Este usuário não foi alterado.'})
    try:
        if usuario_a_alterar['nome']:
            autor.nome =usuario_a_alterar['nome']        
    except:
        pass
    try:
        if usuario_a_alterar['email']:
            autor.email =usuario_a_alterar['email']
    except:
        pass
    try:
        if usuario_a_alterar['senha']:
            autor.senha =usuario_a_alterar['senha']
    except:
        pass
    
    db.session.commit()

    return jsonify({'Mensagem': f'Este usuário, {autor.nome}, foi alterado.'})
# ROTA DE AUTOR - DELETE
@app.route('/autores/<int:id_autor>', methods=['DELETE'])
def deletar_autor(id_autor):
    usuario_a_deletar = Autor.query.filter_by(id_autor=id_autor).first()
    if not usuario_a_deletar:
        return jsonify({'Mensagem': 'Este usuário não foi deletado.'})
    db.session.delete(usuario_a_deletar)
    db.session.commit()

    return jsonify({'Mensagem': f'Este usuário, {usuario_a_deletar}, foi deletado.'})

'''
'''
app.run(port=portaLocal[0], host='localhost', debug=True)