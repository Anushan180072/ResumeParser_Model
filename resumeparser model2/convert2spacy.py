import spacy
import json
from spacy.tokens import DocBin
import itertools
import sys
from pymongo import MongoClient

filename = "dev"
if len(sys.argv) > 1:
    filename = sys.argv[1]

training_data_json_file = f"{filename}.json"
training_data_json = []
empty_tds = []
training_data = []

client = MongoClient("mongodb://localhost:27017")

db = client["resumeparser"]

collection = db["tds"]

# training_data_json = list(collection.find({}).limit(600))
training_data_json = list(collection.find({}).skip(600))
training_data_len = len(training_data_json)
for td in training_data_json:
    text = td["text"]
    entities = td["entities"]
    if len(entities) == 0:  # means no entities marked
        empty_tds.append(text)
        continue

    # remove duplicates from list of entities

    entities.sort()
    unique_entities = [ent for ent, _ in itertools.groupby(entities)]
    training_data.append((text, unique_entities))

# print(training_data)

nlp = spacy.blank("en")  
db = DocBin()
skipped = 0
total = 0

for text, entities in training_data:
    doc = nlp.make_doc(text) 
    valid_ents = []
    try:
        for start, end, label in entities:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            total += 1
            if (
                span is None
                or span.text.startswith(" ")
                or span.text.endswith(" ")
                or span.text != span.text.strip()
            ):
                ent_text = text[start:end]
                print(f"⚠  Skipping Entity : {text[0:30]}... {ent_text}")
                skipped += 1

            else:
                valid_ents.append(span)

        # map ents to valid_ents
        doc.ents = valid_ents
        db.add(doc)
    except Exception as ex:
        print("⚠ ", ex)
        skipped += 1

db.to_disk(f"{filename}.spacy")

print("✨ Results:")
print(f"Total Training Data : {training_data_len}")
print(f"Empty TDs : {len(empty_tds)}")
print(f"Failed to Convert : {skipped} / {total} = {skipped/total*100} %")
