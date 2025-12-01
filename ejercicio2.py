martiz = [
    {"area": "1a", "reforestado": False},{"area": "2a", "reforestado": False},{"area": "3a", "reforestado": False},
     {"area": "1b", "reforestado": False},{"area": "2b", "reforestado": False},{"area": "3b", "reforestado": False},
      {"area": "1c", "reforestado": False},{"area": "2c", "reforestado": False},{"area": "3c", "reforestado": False}
      ]


def reforestar(area):
    for i in martiz:
        if i["area"] == area:
            return i["reforestado"][True]

print(reforestar("1b"))
for i in martiz:
    print(i)