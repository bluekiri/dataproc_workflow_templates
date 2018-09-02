# dataproc_workflow_templates
Demo of Dataproc Workflow templates

Clone the repository and edit **quijote_sorted.py** to point to your bucket:

```
rdd = sc.textFile('gs://bk-dataproc-template/quijote.txt')
```

After that, upload the repository to GCS:

```
gsutil cp * gs://...
```
