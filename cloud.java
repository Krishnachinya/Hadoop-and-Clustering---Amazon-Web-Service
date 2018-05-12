package Assignment;


import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
//
//import temperature.SortTemperature;
//import temperature.TempMapper;
//import temperature.TempPartitioner;
//import temperature.TempReducer;

import org.apache.hadoop.io.FloatWritable;


public class cloud {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        try{
                    //for taking the input from user
                    String from = args[2];
                    String to = args[3];
                    Configuration sort = new Configuration();
                    sort.set("from", from);
                    sort.set("to", to);
                    Job job = Job.getInstance(sort,"User_Data");
                    job.setJarByClass(cloud.class);
                    
                    //Mapper Class
                    job.setMapperClass(userMapper.class);
//                  job.setMapOutputKeyClass(FloatWritable.class);
                    job.setMapOutputKeyClass(Text.class);
                    job.setMapOutputValueClass(Text.class);
                    
                    // Need Combiner Class. but for what? think
                    //Partitioner Class
//                  job.setPartitionerClass(TempPartitioner.class);
                    
                    
                    //Reducer Class
                    job.setReducerClass(userReducer.class);
                    job.setOutputKeyClass(Text.class);
                    job.setOutputValueClass(Text.class);
                    
                    //Number of Reducer Tasks to 8 as we are partitioning the 
                    //data in EIGHT parts
                    job.setNumReduceTasks(1);
                    
                    
                    
                
                    
                    
                    
                    
                    //Input for the program
                    FileInputFormat.addInputPath(job,new Path(args[0]));
                    org.apache.hadoop.mapreduce.lib.output.FileOutputFormat.setOutputPath(job, new Path(args[1]));
                    //FileOutputFormat.setOutputPath(job, new Path(args[1]));
                    System.exit(job.waitForCompletion(true) ? 0 :1);    
                }catch(IOException | ClassNotFoundException | InterruptedException ex)
                {
                    ex.printStackTrace();
                }

    }

}







