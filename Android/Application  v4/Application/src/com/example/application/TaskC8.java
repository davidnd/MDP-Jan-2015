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

public class TaskC8 extends Activity {
	private Button btnSaveReturn;
	private Button btnAbortOperation;
	private EditText editTextString1;
	private EditText editTextString2;
	private EditText editTextString3;
	private EditText editTextString4;
	private EditText editTextString5;
	private String StoredString1;
	private String StoredString2;
	private String StoredString3;
	private String StoredString4;
	private String StoredString5;
	SharedPreferences preferences;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_task_c8);		
		
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
        		Intent i=new Intent(TaskC8.this, MainMenu.class);
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
		
		editTextString3 = (EditText) findViewById(R.id.editTextString3);
		editTextString3.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override		
			public void onFocusChange(View v, boolean hasFocus) {			
				//note necc attributes to be added to parent Relativelayout - focusableInTouchMode, clickable @ .xml file
				if (!hasFocus)
					hideKeyboard(v);	 		    	
	        }
		});	
		
		editTextString4 = (EditText) findViewById(R.id.editTextString4);
		editTextString4.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override		
			public void onFocusChange(View v, boolean hasFocus) {			
				//note necc attributes to be added to parent Relativelayout - focusableInTouchMode, clickable @ .xml file
				if (!hasFocus)
					hideKeyboard(v);	 		    	
	        }
		});	
		
		editTextString5 = (EditText) findViewById(R.id.editTextString5);
		editTextString5.setOnFocusChangeListener(new View.OnFocusChangeListener() {
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
		StoredString3 = preferences.getString("key_msg3", "Click Here");
		StoredString4 = preferences.getString("key_msg4", "Click Here");
		StoredString5 = preferences.getString("key_msg5", "Click Here");
		editTextString1.setText(StoredString1);
		editTextString2.setText(StoredString2);
		editTextString3.setText(StoredString3);
		editTextString4.setText(StoredString4);
		editTextString5.setText(StoredString5);
	}
	
	public void saveMsg() {
        super.onPause();
        android.content.SharedPreferences.Editor editor = preferences.edit();
        editor.putString("key_msg1", editTextString1.getText().toString());
        editor.putString("key_msg2", editTextString2.getText().toString());
        editor.putString("key_msg3", editTextString3.getText().toString());
        editor.putString("key_msg4", editTextString4.getText().toString());
        editor.putString("key_msg5", editTextString5.getText().toString());
        editor.commit();
        //System.out.println(preferences.getString("key_msg1", "na"));
        //System.out.println(preferences.getString("key_msg2", "na"));
         
        Toast.makeText(getApplicationContext(), "Commands Saved", Toast.LENGTH_SHORT).show();
    }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.task_c8, menu);
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
