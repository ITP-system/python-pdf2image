FROM public.ecr.aws/lambda/python:3.9

RUN yum -y install poppler-utils

COPY app.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["app.lambda_handler"]
