# crisis_assessments
 <h2>OCR input of MH crisis assessments</h2> <br>
<p>Client presented with 54 months of printed mental health crisis assessments that need(ed) to be analyzed for diagnostic significance. This consisted of 18 three-inch, 3-ring binders of printed materials that needed to be converted into machine-readable format.</p>
<p>I scanned the documents as *.tif files. Each month of data consisted of approximately 75 to 80 records. I scanned the files in batches of twenty records and employed split_tiff.py to separate the multipage TIFF file into individual files.</p>
<p>I then iterated over the individual image files using [PyTesseract](https://pypi.org/project/pytesseract/).</p>
