package Assignment;


import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;

public class userReducer extends Reducer<Text, Text, Text, Text> {
@Override
public void reduce(Text key,Iterable<Text> values, Context context)
{
    try {
    int count=0;
    for(Text val:values)
    {
        count = count+1;
    }
    context.write(new Text(count+""),key);
    }catch (IOException | InterruptedException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
}
}
