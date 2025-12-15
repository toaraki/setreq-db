FROM registry.redhat.io/ubi9/nginx-122
COPY ./index.html /opt/app-root/src/index.html
USER root
RUN chown -R 1001:0 /opt/app-root/src/index.html
USER 1001
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
EXPOSE 8080
