# Static site: nginx serving presentation/ (html/ css/ images/). No build step —
# presentation/html/contrato.html is rendered by presentation/build_contract.py;
# re-run it BEFORE building if the contract draft changed.
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY presentation/ /usr/share/nginx/html/

EXPOSE 80
