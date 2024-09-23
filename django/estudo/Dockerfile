#inicia de uma imagem vazia
FROM node:lts-alpine as build-stage

# Define o diretório de trabalho
WORKDIR /app

#autor
LABEL maintainer="Marlon Bento"

# Copia o conteúdo do projeto 
COPY front-locallibrary /app

#atualizar os pacotes e instalar o npm
#RUN apt-get update && apt-get install -y npm

# Instala as dependências do projeto e bilda
RUN npm install && npm run build

#IMAGEM DO NGINX
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
#copia as configurações
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

#roda depois de o container executar
CMD ["nginx", "-g", "daemon off;" ]

#docker build

# Construir a imagem
#docker build -t front-locallibrary .

# Rodar o container
#docker container run -p 5173:5173 front-locallibrary