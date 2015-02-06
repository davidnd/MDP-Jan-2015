package com.example.application;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class TaskC7 extends Activity {
	private Button btnSaveReturn;
	private Button btnAbortOperation;
	private EditText editTextString1;
	private EditText editTextString2;
	private String StoredString1;
	private String StoredString2;
	SharedPreferences preferences;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_task_c7);		
		
		btnSaveReturn = (Button)findViewById(R.id.btnSaveReturn);
		btnSaveReturn.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		saveMsg();
        		finish();	//return to previous activity TaskC1 or MainMenu
        	}
        });
		
		btnAbortOperation = (Button)findViewById(R.id.btnAbortOperation);
		btnAbortOperation.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(TaskC7.this, MainMenu.class);
        		startActivity(i);     
        	}
        });
		
		editTextString1 = (EditText) findViewById(R.id.editTextString1);
		editTextString1.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override		
			public void onFocusChange(View v, boolean hasFocus) {			
				//note necc attributes to be added to parent Relativelayout - focusableInTouchMode, clickable @ .xml file
				if (!hasFocus)
					hideKeyboard(v);	 		    	
	        }
		});	
		
		editTextString2 = (EditText) findViewById(R.id.editTextString2);
		editTextString2.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override		
			public void onFocusChange(View v, boolean hasFocus) {			
				//note necc attributes to be added to parent Relativelayout - focusableInTouchMode, clickable @ .xml file
				if (!hasFocus)
					hideKeyboard(v);	 		    	
	        }
		});	
	
		preferences = getSharedPreferences("MyMsgFile", 1);
		StoredString1 = preferences.getString("key_msg1", "Click Here");
		StoredString2 = preferences.getString("key_msg2", "Click Here");
		editTextString1.setText(StoredString1);
		editTextString2.setText(StoredString2);
	}
	
	public void saveMsg() {
        super.onPause();
        android.content.SharedPreferences.Editor editor = preferences.edit();
        editor.putString("key_msg1", editTextString1.getText().toString());
        editor.putString("key_msg2", editTextString2.getText().toString());
        editor.commit();
        //System.out.println(preferences.getString("key_msg1", "na"));
        //System.out.println(preferences.getString("key_msg2", "na"));
         
        Toast.makeText(getApplicationContext(), "Commands Saved", Toast.LENGTH_SHORT).show();
    }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.task_c7, menu);
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
	
	public void hideKeyboard(View view) {
		InputMethodManager inputMethodManager =(InputMethodManager)getSystemService(Activity.INPUT_METHOD_SERVICE);
        inputMethodManager.hideSoftInputFromWindow(view.getWindowToken(), 0);
    }
}
