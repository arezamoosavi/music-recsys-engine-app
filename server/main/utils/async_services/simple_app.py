import faust

# redis_server = os.environ.get('REDIS_SERVER')
# kafka_broker = os.environ.get('KAFKA_SERVER')
app = faust.App(
    'math_op',
    broker='kafka://kafka:9092',
    store='redis://redis:6379/0',
    version=1,
    topic_partitions=8,
)


class Add(faust.Record):
    a: int
    b: int

topic = app.topic('adding', value_type=Add)

@app.agent(topic)
async def adding(stream):
    async for value in stream:
        yield value.a + value.b


"""
class Number(faust.Record, serializer='json'):
    x: float
    
math_topic = app.topic("operations", value_type=Number)

@app.agent(math_topic)
async def process(numbers: faust.Stream[Number]) -> float:
    async for n in numbers:
        yield await summ(n)
        

async def summ(x):
    await powwer(x+x)

async def powwer(x):
    await halff(x**x)

async def halff(x):
    return x/2

"""