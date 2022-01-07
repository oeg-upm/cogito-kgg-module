# Load Virtuoso Triple Store Endpoint

```
docker pull openlink/virtuoso-opensource-7
```

```
sudo docker run --name my_virtdb --env DBA_PASSWORD=mysecret -p 1111:1111 -p 8890:8890 --volume 'pwd':/database -d openlink/virtuoso-opensource-7:latest
```