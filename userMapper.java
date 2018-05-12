package Assignment;

import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Mapper.Context;

import com.sun.xml.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

public class userMapper extends Mapper<LongWritable,Text,Text,Text > {
    private String State;
    private float Age;
    private String[] columns;
    static int count=0;
    
    @Override
    public void map(LongWritable key, Text value,Context context)
    {
        
        try {
        Configuration conf = context.getConfiguration();
        int from = Integer.parseInt(conf.get("from"));
        int to = Integer.parseInt(conf.get("to"));
            
        String line = value.toString();
        columns = line.toString().split(",(?=(?:(?:[^\"\']*\"[^\"\']*\")|(?:[^\'\"]*\'[^\'\"]*))*[^\"]*$)");
        
//      System.out.println("Column Number is"+i);
    
//      System.out.println("Column zero is"+columns[0]);
//      System.out.println("Column one is"+columns[21]);
//      
        if(!columns[0].contains("Gender"))
        {
            State = columns[8];
            Age = Float.parseFloat(columns[21]);
        //year = line.substring(15,26);
        //temperature = Float.parseFloat(line.substring(27,35));
        
            if(State.equalsIgnoreCase("TX"))
            {
                if(Age > from && Age < to)
                {
                    if(count<5)
                    {
                        count++;
                        System.out.println(Arrays.toString(columns));
                    }
                    context.write(new Text(""),new Text(State));
                }
            }
        }
        }catch (IOException | InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        //System.out.println("Hello error is here"+value.toString()+columns);
        }
        
    }

}
