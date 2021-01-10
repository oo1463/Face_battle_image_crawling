from multiprocessing import Process
import image_preprocess.image_crawling
import os

image_preprocess.image_crawling.mx_image_count = 400
image_preprocess.image_crawling.search_terms = ['류준열', '빅뱅 태양', '임영웅', '광희', '최다니엘', '장도연', 'aoa 지민', '김연아', '채영', '개그우먼 김지민']
max_process_queue_size = 4

if __name__ == "__main__":

    job_queue = []
    for search_term in image_preprocess.image_crawling.search_terms:
        if len(job_queue) >= max_process_queue_size:
            for i in range(max_process_queue_size):
                job_queue[i].join()
            job_queue = []

        process = Process(target=image_preprocess.image_crawling.crawling_start, args=(search_term,))
        process.start()
        job_queue.append(process)
        print(process)


    print("job finished")
