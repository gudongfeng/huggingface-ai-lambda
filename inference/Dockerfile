ARG FUNCTION_DIR="/function"

FROM python:3.10 as build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
COPY *.py ${FUNCTION_DIR}

# Install the function's dependencies
RUN pip install --target ${FUNCTION_DIR} torch torchvision torchaudio
RUN pip install --target ${FUNCTION_DIR} transformers
RUN pip install --target ${FUNCTION_DIR} awslambdaric

FROM python:3.10-slim

# Include global arg in this stage of the build
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

# This will get replaced by the proper handler by the CDK script
CMD [ "summarization.handler" ]
