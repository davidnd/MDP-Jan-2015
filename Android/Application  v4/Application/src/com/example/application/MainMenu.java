package com.example.application;

import android.support.v7.app.ActionBarActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainMenu extends ActionBarActivity {
	Button bc1;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main_menu);	
		
		//navigate to TaskC1.java
        bc1=(Button)findViewById(R.id.button1);
        bc1.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(MainMenu.this,TaskC1.class);
        		startActivity(i);
        	}
        });    
        
		//navigate to TaskC2.java
        bc1=(Button)findViewById(R.id.button2);
        bc1.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(MainMenu.this,TaskC8.class);
        		startActivity(i);
        	}
        }); 
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main_menu, menu);
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

	//http://code.tutsplus.com/tutorials/android-interface-design_basic-buttons--mobile-3869
  	//display pop-up
  	public void infoc1(View view)
  	{
  		Toast.makeText(this, "Task C.1 - Transmit & receive text strings over the Bluetooth comm link." + "\n" + "Task C.2 - Scan, select & connect with Bluetooth device." + "\n" + "Task C.3 - Navigate robot Forward, Left and Right." + "\n" + "Task C.4 - Indicate current status of robot." + "\n" + "Task C.5 - Update Robot Start Coordinates to PC." + "\n" + "Task C.6 - 2D display of maze environment." + "\n" + "Task C.7 - Manual / Auto graphical update to maze." + "\n" + "Task C.9 - Robust connectivity with Bluetooth device.", Toast.LENGTH_LONG).show();
  	}

  	public void infoc2(View view)
  	{
  		Toast.makeText(this, "Task C.8 - Persistent user-configurable commands to Robot", Toast.LENGTH_LONG).show();
  	}
  	
  	public void infoc3(View view)
  	{
  		Toast.makeText(this, "Task C.10 - Extension beyond the basics (tilt sensing).", Toast.LENGTH_LONG).show();
  	}
}
