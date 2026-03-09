import aiohttp
import asyncio
import time


async def fetch(session, url):
    start_time = time.perf_counter()
    async with session.get(url) as response:
        end_time = time.perf_counter()
        duration = end_time - start_time
        results = {
            "status_code": response.status,
            "response_time": duration,
            "url": url  
        }
        return results
        
        
async def health_check(urls):
    connector = aiohttp.TCPConnector(verify_ssl=False)
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results
    



if __name__ == "__main__":
    
    urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/500", "https://httpbin.org/delay/2"]
    results = asyncio.run(health_check(urls))
    print(results)