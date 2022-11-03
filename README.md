# url-shortener
is a shotener for urls large

https://urlpst.herokuapp.com/s/dc

postgres://wwkgrrgkackczx:6ab9098bb289f8f8f562477a92584b62fe553705f0d846e64a5cafb4aaedbb1b@ec2-3-220-207-90.compute-1.amazonaws.com:5432/dc8sbpl9l91mqf

psql postgres://wwkgrrgkackczx:6ab9098bb289f8f8f562477a92584b62fe553705f0d846e64a5cafb4aaedbb1b@ec2-3-220-207-90.compute-1.amazonaws.com:5432/dc8sbpl9l91mqf

INSERT INTO urls (id, url) VALUES('semana', 'https://www.semana.com/semana-tv/vicky-en-semana/articulo/me-estas-faltando-al-respeto-durisimo-agarron-entre-katherine-miranda-y-su-denunciante-jonathan-silva-por-querer-que-las-iglesias-paguen-impuestos/202251/?utm_medium=Social&utm_campaign=echobox&utm_source=Facebook&fbclid=IwAR2kkbFSpqxoBAv_cLMRb-y4LKEE28qhv6Fq4JPa6tU1zoUJQ2up3pNj3ic#Echobox=1666893274');

INSERT INTO urls (id, url) VALUES('dc', 'https://www.youtube.com/channel/UCmYmlHc-3_MHLigi-lFel-Q');

heroku login -i

curl -d '{"url":"https://www.valledelcauca.gov.co/publicaciones/73447/transparencia-y-acceso-a-la-informacion-publica/"}' -H "Content-Type: application/json" -X POST https://urlpst.herokuapp.com/shorten-url

https://urlpst.herokuapp.com/s/QVIaEf
