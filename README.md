# How to deploy to aws
- `cdk bootstrap && cdk deploy`

# How to run the docker file locally

- `docker build -t docker-image:test .`
```
docker run -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
    --entrypoint /aws-lambda/aws-lambda-rie \
    docker-image:test \
        /usr/local/bin/python -m awslambdaric translator.handler
```
- `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"voiceUrl":"https://s3.us-west-2.amazonaws.com/gudongfeng.me/voice-source-files/mlk.flac"}'`