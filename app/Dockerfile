FROM python:3.11-slim
WORKDIR /app
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 --no-create-home appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY webapp.py .
RUN chown -R appuser:appgroup /app
USER appuser
EXPOSE 8080
CMD ["python", "webapp.py"]