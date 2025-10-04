import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int jobLen = jobs.length;
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        PriorityQueue<Job> waitQueue = new PriorityQueue<>();

        int currTime = 0;
        int index = 0;
        int total = 0;

        while (index < jobLen || !waitQueue.isEmpty()) { 
            while (index < jobLen && jobs[index][0] <= currTime) { 
                waitQueue.offer(new Job(jobs[index][0], jobs[index][1]));
                index++;
            }

            if (waitQueue.isEmpty()) { 
                currTime = jobs[index][0];
            } else {
                Job job = waitQueue.poll();
                currTime += job.i;
                total += (currTime - job.s);
            }
        }

        return total / jobLen;
    }
    
    class Job implements Comparable<Job> {
        
        int s; 
        
        int i; 

        public Job(int s, int i) {
            this.s = s;
            this.i = i;
        }

        @Override
        public int compareTo(Job job) {
            return this.i - job.i;
        }
    }
}