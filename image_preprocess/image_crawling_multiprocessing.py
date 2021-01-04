from multiprocessing import Process
import image_preprocess.image_crawling

image_preprocess.image_crawling.mx_image_count = 400
image_preprocess.image_crawling.search_terms = ['원빈', '장동건', '강동원', '현빈', '정우성', '송중기', '차은우', '소지섭', '조인성']
max_process_queue_size = 4

if __name__ == "__main__":

    job_queue = []
    for search_term in image_preprocess.image_crawling.search_terms:
        if len(job_queue) >= max_process_queue_size:
            job_queue[0].join()
            job_queue[1].join()

        process = Process(target=image_preprocess.image_crawling.crawling_start, args=(search_term,))
        process.start()
        job_queue.append(process)
        print(process)


