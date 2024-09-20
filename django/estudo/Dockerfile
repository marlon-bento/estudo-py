#inicia de uma imagem vazia
FROM scratch

#autor
LABEL maintainer="Marlon Bento"

#atualizar os pacotes e instalar o npm
RUN apt-get update && apt-get install -y npm

#expondo a porta do vue
EXPOSE 5173

COPY ./front-locallibrary vue 

#roda depois de o container executar
CMD ["npm run", "dev"]