package com.example.application;

import android.support.v7.app.ActionBarActivity;
import android.content.DialogInterface;
import android.content.DialogInterface.OnClickListener;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends ActionBarActivity implements OnClickListener{
	Button b1;

	@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //setContentView(R.layout.activity_main_menu);
        //setContentView(R.layout.activity_task_c1);
        //setContentView(R.layout.activity_task_c2);

        //http://www.higherpass.com/Android/Tutorials/Working-With-Images-In-Android/
        ImageView image = (ImageView) findViewById(R.id.test_image);       
        
        //navigate to MainMenu.java
        //http://stackoverflow.com/questions/13194081/how-to-open-a-second-activity-on-click-of-button-in-android-app
        b1=(Button)findViewById(R.id.button1);
        b1.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(MainActivity.this,MainMenu.class);
        		startActivity(i);
        	}
        });              
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
	
    @Override
	public void onClick(DialogInterface dialog, int which) {
		// TODO Auto-generated method stub
		
	}

 }
