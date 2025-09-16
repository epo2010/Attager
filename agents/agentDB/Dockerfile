FROM redis:7-alpine
COPY dump.rdb /data/dump.rdb
CMD ["redis-server", "--appendonly", "yes"]
