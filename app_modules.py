import chromadb

def return_results(collection):
    
    results = collection.query(
      query_texts=["Show formcrs for eci 12345"], # Chroma will embed this for you
      n_results=2 # how many results to return
    )
    return results

def create_db():
    client = chromadb.Client()
    collection = client.create_collection(name="my_collection")
    collection.add(
        documents=["{'eci': '12345', 'attestationid': 'A12345'}",
                   "{'eci': '12345', 'formcrsid': 'f34567'}"],
        ids=["1", "2"]
    )
    return collection