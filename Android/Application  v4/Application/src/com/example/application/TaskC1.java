package com.example.application;

import model.Robot;
import draw.Draw;

import java.util.Set;

import android.annotation.SuppressLint; 
import android.app.ActionBar.LayoutParams;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnTouchListener;
import android.view.inputmethod.InputMethodManager;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

public class TaskC1 extends Activity implements OnTouchListener, SensorEventListener{	
	private Button goMainMenu;
	private Button btnActivateBT;
	private Button btnDeactivateBT;
	private Button btnListPairedDevices;
	private Button btnNewSearch;	
	private Button btnSend;		
	private Button btnForward;
	//private Button btnRotateOpposite;
	private Button btnRotateLeft;
	private Button btnRotateRight;
	private Button btnGoPersistence;
	private Button btnSendStoredString1;
	private Button btnSendStoredString2;
	private Button btnSendStoredString3;
	private Button btnSendStoredString4; 
	private Button btnSetCoordinate;
	private Button btnUpdateMap;	
	
	private ToggleButton tbTilt;
	private ToggleButton tbAutoManual;
	private SensorManager senSensorManager;
    private Sensor senAccelerometer;
    
	boolean initalized = false;
    boolean up = false;
    boolean down = false;
    boolean left = false;
    boolean right = false;
    
	private TextView tiltDirection;
	private TextView robotStatus;	
	private TextView textViewNavigation;
	private TextView textViewOtherModes;
	private TextView editTextBTStatus;	
	private ListView myListView;
	private ListView mConversationView;
	private EditText input;
	private TextView textViewSetCoordinate;
	private TextView textViewXcoord;
	private EditText editTextXcoord;
	private TextView textViewYcoord;
	private EditText editTextYcoord;
	
	Robot robot;
	Draw draw;
	
	SharedPreferences preferences;
	String StoredString1;
	String StoredString2;
	String StoredString3;
	String StoredString4;
	
	private Handler mdHandler; //for Task C.3-5, 'mHandler' for Task C.1-2
		
	//member fields
    private BluetoothAdapter myBluetoothAdapter = null;  
	private ArrayAdapter<String> BTArrayAdapter;
    private ArrayAdapter<String> mConversationArrayAdapter;
	private Set<BluetoothDevice> pairedDevices;
    public BluetoothService myBTservice;	

	//class variables
	private static final String TAG = "BluetoothChat";
    private static final boolean D = true;
    //public static final String MSG_NAME = "MyMsgFile";
	public static final int UP = 0;
	public static final int RIGHT = 1;
	public static final int DOWN = 2;
	public static final int LEFT = 3;
	
	private int xcoordinate;
	private int ycoordinate;
	
    // msg types sent from the BluetoothService Handler
    public static final int MESSAGE_STATE_CHANGE = 1;
    public static final int MESSAGE_READ = 2;
    public static final int MESSAGE_WRITE = 3;
    public static final int MESSAGE_DEVICE_NAME = 4;
    public static final int MESSAGE_TOAST = 5;
    public static final int STATE_NONE = 0;       // we're doing nothing
    public static final int STATE_LISTEN = 1;     // now listening for incoming connections
    public static final int STATE_CONNECTING = 2; // now initiating an outgoing connection
    public static final int STATE_CONNECTED = 3;  // now connected to a remote device    

    // Key names received from the BluetoothService Handler
    public static final String DEVICE_NAME = "device_name";
    public static final String TOAST = "toast";
    public static String EXTRA_DEVICE_ADDRESS = "device_address";
    
    // Intent request codes
    private static final int REQUEST_CONNECT_DEVICE_SECURE = 1;
    private static final int REQUEST_CONNECT_DEVICE_INSECURE = 2;
    private static final int REQUEST_ENABLE_BT = 3;

    // Name of the connected device
    private String mConnectedDeviceName = "test";    
    private String selectedBTNetwork = "";
    
    // String buffer for outgoing messages
    private StringBuffer mOutStringBuffer;   
    
    //C.3 - C.5
    /////////////////////////////////////////////////////////////////
 	String easyPuzzle = "11111111111111111111" + "11111111111111111111" +
 						"11111111111111111111" + "11011100000000000111" +
 						"11011101111111110111" + "11011101111111110111" +
 						"11011101111111110111" + "11111101111111110111" + 
 						"11111101111111110111" + "11111101111111110111" +
 						"11101101111111110111" + "11101101111111110111" +
 						"11111111111111110111" + "11111111111111111111" +
 						"11111111111111111111";
 	
 	String newPuzzle = "0 0 0 " + "22200000000200022100"
                                + "00000000000000000000"
                                + "01000221000000001000"
                                + "00000001000000022100"
                                + "00000000002010000000"
                                + "00000001100000001002"
                                + "00000000000111200000"
                                + "00000000002010000000"
                                + "00000001000000000000"
                                + "20100000000000011100"
                                + "00111001020000000000"
                                + "00202000000000000002"
                                + "00000000000020200000"
                                + "00001222020000000000"
                                + "00102000000000000102" ;
 	
 	@Override	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_task_c1);	
				
		//Task C.3 - C.5
		draw = (Draw) findViewById(R.id.map);
		draw.setPuzzle(newPuzzle);

		robot = draw.robot;
		initalized = false;				
		
		preferences = getSharedPreferences("MyMsgFile", 0);		
		StoredString1 = preferences.getString("key_msg1", "na");
		StoredString2 = preferences.getString("key_msg2", "na");
		StoredString3 = preferences.getString("key_msg3", "na");
		StoredString4 = preferences.getString("key_msg4", "na");

		editTextBTStatus = (TextView) findViewById (R.id.editTextBTStatus);	
		textViewNavigation = (TextView) findViewById(R.id.textViewNavigation);
		textViewOtherModes = (TextView) findViewById(R.id.textViewOtherModes);
		tiltDirection = (TextView) findViewById(R.id.tiltDirection);
		robotStatus = (TextView) findViewById(R.id.robotStatus);
		tbAutoManual = (ToggleButton) findViewById(R.id.tbAutoManual);
		tbTilt = (ToggleButton) findViewById(R.id.tbTilt);
		
		//tbTilt.setChecked(true);

		btnUpdateMap = (Button) findViewById(R.id.btnUpdateMap);		
		btnSend = (Button)findViewById(R.id.btnSend);
		btnForward = (Button)findViewById(R.id.btnForward);
		//btnRotateOpposite = (Button)findViewById(R.id.btnRotateOpposite);
		btnRotateLeft = (Button)findViewById(R.id.btnRotateLeft);
		btnRotateRight = (Button)findViewById(R.id.btnRotateRight);		
		
		//Task C.5 change to other relevant ids and continue code setcoordinate
		btnSetCoordinate = (Button)findViewById(R.id.btnSetCoordinate);
		textViewSetCoordinate = (TextView) findViewById(R.id.textViewSetCoordinate);
		textViewXcoord = (TextView)findViewById(R.id.textViewXcoord);
		editTextXcoord = (EditText)findViewById(R.id.editTextXcoord);
		textViewYcoord = (TextView)findViewById(R.id.textViewYcoord);
		editTextYcoord = (EditText)findViewById(R.id.editTextYcoord);
		
		btnSetCoordinate.setOnClickListener(new OnClickListener(){				
			public void onClick(View v) {	
				EditText xcoord = (EditText) findViewById(R.id.editTextXcoord);
				String message1 = xcoord.getText().toString();
				int xcoordinate = Integer.parseInt(message1);
				EditText ycoord = (EditText) findViewById(R.id.editTextYcoord);
				String message2 = ycoord.getText().toString();
				int ycoordinate = Integer.parseInt(message2);
				//Set to map
				Robot r1 = new Robot();
				r1.setX(xcoordinate);
				r1.setY(ycoordinate);	
			}
		});				
		
		btnSendStoredString1 = (Button)findViewById(R.id.btnSendStoredString1);
		btnSendStoredString1.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		sendStoredStrings1();
        	}
        });
		btnSendStoredString2 = (Button)findViewById(R.id.btnSendStoredString2);
		btnSendStoredString2.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		sendStoredStrings2();
        	}
        });
		btnSendStoredString3 = (Button)findViewById(R.id.btnSendStoredString3);
		btnSendStoredString3.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		sendStoredStrings3();
        	}
        });
		btnSendStoredString4 = (Button)findViewById(R.id.btnSendStoredString4);
		btnSendStoredString4.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		sendStoredStrings4();
        	}
        });
		btnGoPersistence = (Button)findViewById(R.id.btnGoPersistence);
		btnGoPersistence.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(TaskC1.this, TaskC8.class);
        		startActivity(i);
        	}
        });    

		btnForward.setOnTouchListener(this);
		//btnRotateOpposite.setOnTouchListener(this);
		btnRotateLeft.setOnTouchListener(this);
		btnRotateRight.setOnTouchListener(this);
		
		//not load tilt sensing yet
		senSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);		
		
		mdHandler = new Handler();		
		
		//navigate to MainMenu.java
		goMainMenu = (Button)findViewById(R.id.btnMainMenu);
		goMainMenu.setOnClickListener(new android.view.View.OnClickListener()
        {        
        	public void onClick(View v)
        	{
        		Intent i=new Intent(TaskC1.this, MainMenu.class);
        		startActivity(i);
        	}
        });     
		
    	/*
    	//apply onfocuschange instd of onclick
		final EditText et = (EditText) findViewById(R.id.editText1);
		et.setOnClickListener(new View.OnClickListener() {
	    @Override
	    public void onClick(View v) {
        	//activate soft keyboard, by force
	        InputMethodManager imm = (InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
	        imm.showSoftInput(et, InputMethodManager.SHOW_IMPLICIT);   
	    	}
	    });		
		*/			
		
		input = (EditText) findViewById(R.id.editText1);
		input.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override		
			public void onFocusChange(View v, boolean hasFocus) {			
				//note necc attributes to be added to parent Relativelayout - focusableInTouchMode, clickable @ .xml file
				if (!hasFocus)
					hideKeyboard(v);	 		    	
	        }
		});		
		
		//Task C.1 & C.2 - Set up bt
		myBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();	
		myBTservice = new BluetoothService(this, mHandler);
		setupChat();
		
		// Initialize conversation thread
    	mConversationArrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1);
    	mConversationView = (ListView) findViewById(R.id.listReceived);
    	mConversationView.setAdapter(mConversationArrayAdapter);	
		
		// create the arrayAdapter that contains the BTDevices, and set it to the ListView		
		BTArrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1);						
		myListView = (ListView)findViewById(R.id.listView1);	
		myListView.setAdapter(BTArrayAdapter);		
				
		//check if bt supported
		if(myBluetoothAdapter == null) {				
			editTextBTStatus.setText("Not Supported");		          
			Toast.makeText(getApplicationContext(),"Your device does not support Bluetooth", Toast.LENGTH_LONG).show();			     
		}
		else {
			//editTextStatus = (TextView) findViewById (R.id.editTextStatus);	
			editTextBTStatus.setText("Disabled");
			
			btnActivateBT = (Button) findViewById(R.id.btnActivateBT);
			btnActivateBT.setOnClickListener(new OnClickListener() {
				@Override
				public void onClick(View v) {	
					btnActivateBT.setVisibility(View.GONE);						
					on(v);
				}			
			});
			
			btnDeactivateBT = (Button)findViewById(R.id.btnDeactivateBT);
			btnDeactivateBT.setOnClickListener(new OnClickListener() {
				@Override
	            public void onClick(View v) {
					btnActivateBT.setVisibility(View.VISIBLE);					
					off(v);
				}
			});			
						
			btnListPairedDevices = (Button)findViewById(R.id.btnListPairedDevices);
			btnListPairedDevices.setOnClickListener(new OnClickListener() {			     	    
				@Override
				public void onClick(View v) {
					listPairedDevices(v);
				}
			});
					
			btnNewSearch = (Button)findViewById(R.id.btnNewSearch);
			btnNewSearch.setOnClickListener(new OnClickListener(){				
				@Override
				public void onClick(View v) {
					find(v);
				}
			});											
		
			//BT already on when app loads
			if (myBluetoothAdapter.isEnabled()){
				Toast.makeText(getApplicationContext(),"Bluetooth already on" , Toast.LENGTH_SHORT).show();
					
				//clear listview previously displayed
				BTArrayAdapter.clear();	
				mConversationArrayAdapter.clear();

				editTextBTStatus.setText("Enabled");
				myListView.setVisibility(View.VISIBLE);	
				mConversationView.setVisibility(View.VISIBLE);
				btnActivateBT.setVisibility(View.GONE);
				btnDeactivateBT.setVisibility(View.VISIBLE);   
				btnListPairedDevices.setVisibility(View.VISIBLE);
				btnNewSearch.setVisibility(View.VISIBLE);	
			}			
			myListView.setOnItemClickListener(new OnItemClickListener(){
				@Override
				public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
					//check if listview is empty
		            //connect to device when listview item is click		
					if (BTArrayAdapter != null){								
						myBluetoothAdapter.cancelDiscovery();

						/*
						//initiate pairing
						try {
							final String info = ((TextView) view).getText().toString();
							String address = info.substring(info.length()-17);
							BluetoothDevice device = myBluetoothAdapter.getRemoteDevice(address);
							BluetoothSocket socket = null;	
							selectedBTNetwork = device.getName();
							socket =(BluetoothSocket) device.getClass().getMethod("createRfcommSocket", new Class[] {int.class}).invoke(device,1);
							socket.connect();
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (IllegalArgumentException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (IllegalAccessException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (InvocationTargetException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						} catch (NoSuchMethodException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						*/					
						
						//apply MDP-AMDT tool b4 attempting to conn via bt
						String temp = (String) myListView.getItemAtPosition(position);						
						String deviceAdd = null;
						deviceAdd = temp.substring(temp.length()-17);
						BluetoothDevice device = myBluetoothAdapter.getRemoteDevice(deviceAdd);
						selectedBTNetwork = device.getName();
					    
						//do initialize var else function will not be called
					    if (myBTservice == null)
					    	setupChat();				    
					    
					    Intent intent = new Intent();
			            intent.putExtra(EXTRA_DEVICE_ADDRESS, deviceAdd);
				        connectDevice(intent,true);
					}					
				}
			});				
		}		
	}//end method	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.task_c1, menu);
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

	//methods across Task C.1, C.2
	public void on(View view){
	if (!myBluetoothAdapter.isEnabled()) {		
		//clear listview previously displayed
		BTArrayAdapter.clear();	
		mConversationArrayAdapter.clear();
		
		Intent turnOnIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
		startActivityForResult(turnOnIntent, REQUEST_ENABLE_BT);
		Toast.makeText(getApplicationContext(),"Bluetooth turned on" , Toast.LENGTH_LONG).show();	

		myListView.setVisibility(View.VISIBLE);
		mConversationView.setVisibility(View.VISIBLE);
		btnDeactivateBT.setVisibility(View.VISIBLE);   
		btnListPairedDevices.setVisibility(View.VISIBLE);
		btnNewSearch.setVisibility(View.VISIBLE);		
	}
	else{	
		Toast.makeText(getApplicationContext(),"Bluetooth is already on", Toast.LENGTH_LONG).show();
		
		myListView.setVisibility(View.VISIBLE);
		mConversationView.setVisibility(View.VISIBLE);
		btnDeactivateBT.setVisibility(View.VISIBLE);   
		btnListPairedDevices.setVisibility(View.VISIBLE);
		btnNewSearch.setVisibility(View.VISIBLE);	
	}
}
  
	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		//super.onActivityResult(requestCode, resultCode, data);
		
		if(requestCode == REQUEST_ENABLE_BT){
	  		if(myBluetoothAdapter.isEnabled() ) {
	  			editTextBTStatus.setText("Enabled");
	  			
	  			if (myBTservice == null)
	  				setupChat();
	  		} 
	  		else {  	  			
	  			myListView.setVisibility(View.GONE);
				mConversationView.setVisibility(View.GONE);
	  			
	  			btnActivateBT.setVisibility(View.VISIBLE);	  			
	  			btnDeactivateBT.setVisibility(View.GONE);   
	  			btnListPairedDevices.setVisibility(View.GONE);
	  			btnNewSearch.setVisibility(View.GONE);	
	  			btnSend.setVisibility(View.GONE);
	  			btnForward.setVisibility(View.GONE);
	  			//btnRotateOpposite.setVisibility(View.GONE);
	  			btnRotateLeft.setVisibility(View.GONE);
	  			btnRotateRight.setVisibility(View.GONE);
	  			input.setVisibility(View.GONE);
	  			btnGoPersistence.setVisibility(View.GONE);
	  			btnSendStoredString1.setVisibility(View.GONE);
	  			btnSendStoredString2.setVisibility(View.GONE);
	  			btnSendStoredString3.setVisibility(View.GONE);
	  			btnSendStoredString4.setVisibility(View.GONE);
	  			//1234
	  			btnSetCoordinate.setVisibility(View.GONE);
	  			textViewSetCoordinate.setVisibility(View.GONE);
	  			textViewXcoord.setVisibility(View.GONE);
	  			editTextXcoord.setVisibility(View.GONE);
	  			textViewYcoord.setVisibility(View.GONE);
	  			editTextYcoord.setVisibility(View.GONE);
	  			
	  			editTextBTStatus.setText("Disabled");
	  			
	  			//kill process & return to MainMenu
	  			//finish();
	  		}             
	  	}
		
		if(requestCode == REQUEST_CONNECT_DEVICE_SECURE){
			// device to connect returned		
			if (resultCode == Activity.RESULT_OK) {						
				Log.d("test", "ok");
				connectDevice(data, true);
			}
		}
		
		if(requestCode == REQUEST_CONNECT_DEVICE_INSECURE){
			// device to connect returned
			if (resultCode == Activity.RESULT_OK) {
				connectDevice(data, false);
			}
		}
	}

	public void listPairedDevices(View view){		
		//stop discovery
		myBluetoothAdapter.cancelDiscovery();
		
		//clear listview previously displayed
		BTArrayAdapter.clear();		
		
		// get paired devices
	    pairedDevices = myBluetoothAdapter.getBondedDevices();    
        
	    // place devices to adapter
	    if (pairedDevices.size() > 0){
	    	for (BluetoothDevice device : pairedDevices)		    	
	    		BTArrayAdapter.add(device.getName()+ "\n" + device.getAddress());	    
	    }	
	    Toast.makeText(getApplicationContext(),"Showing list of paired devices found", Toast.LENGTH_SHORT).show();
	    
	    if (pairedDevices.size() == 0)
	    	Toast.makeText(getApplicationContext(),"No paired devices found", Toast.LENGTH_SHORT).show();
	    
	    //disable listview - because pairing is manual, we dont want users to pair via selected item but view only
	    myListView.setEnabled(false);
	}
	    
    final BroadcastReceiver bReceiver = new BroadcastReceiver() {
		public void onReceive(Context context, Intent intent) {
			String action = intent.getAction();

	    	// When discovery finds a device
	    	if (BluetoothDevice.ACTION_FOUND.equals(action)) {
	    		// Get the BluetoothDevice object from the Intent
	    		BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);

	    		// add the name and the MAC address of the object to the arrayAdapter
	    		BTArrayAdapter.add(device.getName() + "\n" + device.getAddress());
	    		BTArrayAdapter.notifyDataSetChanged();
            }
	    	else if(BluetoothAdapter.ACTION_DISCOVERY_FINISHED.equals(action)){
            	unregisterReceiver(this);
            	myBluetoothAdapter.cancelDiscovery();
            	Toast.makeText(context, "discovery has ended!", Toast.LENGTH_SHORT).show();
            }
	    	else if (BluetoothDevice.ACTION_ACL_CONNECTED.equals(action)) {
	    		//Do something if connected
	    		//Toast.makeText(getApplicationContext(), "BT Connected", Toast.LENGTH_SHORT).show();
	    	}
	    }
	}; 	
		
	public void find(View view) {		
		myListView.setEnabled(true);
		if (myBluetoothAdapter.isDiscovering()) {			
			// the button is pressed when it discovers, so cancel the discovery
			myBluetoothAdapter.cancelDiscovery();
	    }
	    else {
	    	BTArrayAdapter.clear();
	        myBluetoothAdapter.startDiscovery();
	        registerReceiver(bReceiver, new IntentFilter(BluetoothDevice.ACTION_FOUND));
	    }
		Toast.makeText(getApplicationContext(),"Showing all devices", Toast.LENGTH_SHORT).show();
	}
		
	public void off(View view){
		myBluetoothAdapter.disable();
		editTextBTStatus.setText("Disconnected");
	    Toast.makeText(getApplicationContext(),"Bluetooth turned off", Toast.LENGTH_LONG).show();
	    		
	    myListView.setVisibility(View.GONE);
		mConversationView.setVisibility(View.GONE);
		btnDeactivateBT.setVisibility(View.GONE);   
		btnListPairedDevices.setVisibility(View.GONE);
		btnNewSearch.setVisibility(View.GONE);	
		btnSend.setVisibility(View.GONE);
		btnForward.setVisibility(View.GONE);
		//btnRotateOpposite.setVisibility(View.GONE);
		btnRotateLeft.setVisibility(View.GONE);
		btnRotateRight.setVisibility(View.GONE);
		input.setVisibility(View.GONE);
		textViewNavigation.setVisibility(View.GONE);
		textViewOtherModes.setVisibility(View.GONE);
		btnUpdateMap.setVisibility(View.GONE);
		tbTilt.setVisibility(View.GONE);
		tbAutoManual.setVisibility(View.GONE);				
		draw.setVisibility(View.GONE);
		btnGoPersistence.setVisibility(View.GONE);
		btnSendStoredString1.setVisibility(View.GONE);
		btnSendStoredString2.setVisibility(View.GONE);
		btnSendStoredString3.setVisibility(View.GONE);
		btnSendStoredString4.setVisibility(View.GONE);
		//1234
		btnSetCoordinate.setVisibility(View.GONE);
		textViewSetCoordinate.setVisibility(View.GONE);
		textViewXcoord.setVisibility(View.GONE);
		editTextXcoord.setVisibility(View.GONE);
		textViewYcoord.setVisibility(View.GONE);
		editTextYcoord.setVisibility(View.GONE);
    }

	private final Handler mHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
            	case MESSAGE_STATE_CHANGE:
            		if(D) 
            			Log.i(TAG, "MESSAGE_STATE_CHANGE: " + msg.arg1);
                
            		switch (msg.arg1) {
            			case BluetoothService.STATE_CONNECTED:
            				BTArrayAdapter.clear();
            				mConversationArrayAdapter.clear();
            				
            				Toast.makeText(getApplicationContext(), "Connection established", Toast.LENGTH_SHORT).show();
            				
            				btnSend.setVisibility(View.VISIBLE);
            				btnForward.setVisibility(View.VISIBLE);
            				//btnRotateOpposite.setVisibility(View.VISIBLE);
            				btnRotateLeft.setVisibility(View.VISIBLE);
            				btnRotateRight.setVisibility(View.VISIBLE);
            	  			input.setVisibility(View.VISIBLE);     
            	  			textViewNavigation.setVisibility(View.VISIBLE);
            	  			textViewOtherModes.setVisibility(View.VISIBLE);
            	  			btnUpdateMap.setVisibility(View.VISIBLE);
            	  			tbTilt.setVisibility(View.VISIBLE);            	  			
            	  			tbAutoManual.setVisibility(View.VISIBLE);				
            	  			draw.setVisibility(View.VISIBLE);
            	  			btnGoPersistence.setVisibility(View.VISIBLE);
            	  			btnSendStoredString1.setVisibility(View.VISIBLE);
            	  			btnSendStoredString2.setVisibility(View.VISIBLE);
            	  			btnSendStoredString3.setVisibility(View.VISIBLE);
            	  			btnSendStoredString4.setVisibility(View.VISIBLE); 
            	  			//1234
            	  			btnSetCoordinate.setVisibility(View.VISIBLE);
            	  			textViewSetCoordinate.setVisibility(View.VISIBLE);
            	  			textViewXcoord.setVisibility(View.VISIBLE);
            	  			editTextXcoord.setVisibility(View.VISIBLE);
            	  			textViewYcoord.setVisibility(View.VISIBLE);
            	  			editTextYcoord.setVisibility(View.VISIBLE);
            	  			
            	  			tbAutoManual.setChecked(false);
            	  			tbTilt.setChecked(false);      	  			
            	  			break;
            				
            			case BluetoothService.STATE_CONNECTING:     
            				Toast.makeText(getApplicationContext(), "Attempting to connect to " + selectedBTNetwork, Toast.LENGTH_SHORT).show();            				
            				break;
                
            			case BluetoothService.STATE_LISTEN:            				
            				break;
            				
            			case BluetoothService.STATE_NONE:
            		    	BTArrayAdapter.clear();
            		        myBluetoothAdapter.startDiscovery();
            		        registerReceiver(bReceiver, new IntentFilter(BluetoothDevice.ACTION_FOUND));
            		        
            				btnSend.setVisibility(View.GONE);
            				btnForward.setVisibility(View.GONE);
            				//btnRotateOpposite.setVisibility(View.GONE);
            				btnRotateLeft.setVisibility(View.GONE);
            				btnRotateRight.setVisibility(View.GONE);     
            	  			input.setVisibility(View.GONE);              	  			
            	  			textViewNavigation.setVisibility(View.GONE);
            	  			textViewOtherModes.setVisibility(View.GONE);
            	  			btnUpdateMap.setVisibility(View.GONE);
            	  			tbTilt.setVisibility(View.GONE);
            	  			tbAutoManual.setVisibility(View.GONE);				
            	  			draw.setVisibility(View.GONE);
            	  			btnGoPersistence.setVisibility(View.GONE);
            	  			btnSendStoredString1.setVisibility(View.GONE);
            	  			btnSendStoredString2.setVisibility(View.GONE);
            	  			btnSendStoredString3.setVisibility(View.GONE);
            	  			btnSendStoredString4.setVisibility(View.GONE);
            	  			//1234
            	  			btnSetCoordinate.setVisibility(View.GONE);
            	  			textViewSetCoordinate.setVisibility(View.GONE);
            	  			textViewXcoord.setVisibility(View.GONE);
            	  			editTextXcoord.setVisibility(View.GONE);
            	  			textViewYcoord.setVisibility(View.GONE);
            	  			editTextYcoord.setVisibility(View.GONE);
            		        break;
            		}
            		break;
            
            	case MESSAGE_WRITE:
            		byte[] writeBuf = (byte[]) msg.obj;
            		
            		// 	construct a string from the buffer
            		String writeMessage = new String(writeBuf);
            		mConversationArrayAdapter.add("Me:  " + writeMessage);
            		break;
            
            	case MESSAGE_READ:
            		byte[] readBuf = (byte[]) msg.obj;
            		
            		// 	construct a string from the valid bytes in the buffer
            		final String readMessage = new String(readBuf, 0, msg.arg1);           		
            		
            		if (readMessage.startsWith("GRID")) {
    					if (tbAutoManual.isChecked()) {
    						// go push message to draw
    						draw.setPuzzle(readMessage);
    					}
    					else{
    						btnUpdateMap.setOnClickListener(new OnClickListener(){
    							@Override
    							public void onClick(View v) {
    								//String map;
    								//map = draw.getCurrentMap();
    								draw.setPuzzle(readMessage);
    							}    							
    						});
    					}
            		}
    				mConversationArrayAdapter.add(mConnectedDeviceName+":  " + readMessage);
    				Log.i("FRAGMAP", readMessage + "");
    				break;
            		
            	case MESSAGE_DEVICE_NAME:
            		// 	save the connected device's name
            		mConnectedDeviceName = msg.getData().getString(DEVICE_NAME);
            		Toast.makeText(getApplicationContext(), "Connected to "+ mConnectedDeviceName, Toast.LENGTH_SHORT).show();                
            		break;
            		
            	case MESSAGE_TOAST:
            		Toast.makeText(getApplicationContext(), msg.getData().getString(TOAST), Toast.LENGTH_SHORT).show();
            		break;
            }
        }
    };
    
    private void connectDevice(Intent data, boolean secure) {
    	// Get the device MAC address
    	String address = "test";
    	
    	try{    		
    		address = data.getExtras().getString(TaskC1.EXTRA_DEVICE_ADDRESS);    		
	    }
	    catch(Exception e){
	    	Log.d("error","noAdd");
	    }
        		
        // Get the BLuetoothDevice object
    	if (myBluetoothAdapter == null){
    		System.out.println("myBluetoothAdapter is null");
    	}
	
		BluetoothDevice device = myBluetoothAdapter.getRemoteDevice(address);
        
    	// Attempt to connect to the device
        if (device == null)
        	System.out.println("Device is null");
        if (myBTservice == null)
        	System.out.println("BluetoothService is null");
        myBTservice.connect(device, secure);        
    }
    
    private void setupChat() {
    	Log.d(TAG, "setupChat()");

    	btnSend = (Button)findViewById(R.id.btnSend);
    	btnSend.setOnClickListener(new OnClickListener(){				
			@Override
			public void onClick(View v) {	
				EditText et = (EditText) findViewById(R.id.editText1);
                String message = et.getText().toString();
                sendMessage(message);
                et.setText("");
            }
		});			
    	
        // Initialize & perform bt conns
    	myBTservice = new BluetoothService(this, mHandler); 
    	
    	// Initialize the buffer for outgoing messages
        mOutStringBuffer = new StringBuffer("");
    }
    
    private void sendMessage(String message) {
        // Check that we're actually connected before trying anything
        if (myBTservice.getState() != myBTservice.STATE_CONNECTED) {
            Toast.makeText(this, "Not connected", Toast.LENGTH_SHORT).show();
            return;
        }

        // Check if no content to send
        if (message.length() > 0) {
            // Get the message bytes and tell the BluetoothChatService to write
            byte[] send = message.getBytes();
            myBTservice.write(send);

            // Reset out string buffer & clear edittext
            mOutStringBuffer.setLength(0);
            //mOutStringBuffer = new StringBuffer("");
            //input.setText("");
        }
        else {
        	Toast.makeText(this, "Please input string", Toast.LENGTH_SHORT).show();
        }        	
    }
    
    //Task C.9 - tilt direction
    @Override
	public void onSensorChanged(SensorEvent event) {
    	if (!initalized) {
			// tiltMsg.setText("0");
			initalized = true;
		} 
    	else {
			float x = event.values[0];
			float y = event.values[1];
			float z = event.values[2];
			// tiltMsg.setText(x + " " + y + " " + z);

			if (x >= 2.9) {
				sendDirection(0); // left
			} 
			else if (x <= -2.9) {
				sendDirection(1);// right
			} 
			else if (y <= -2.2) {
				sendDirection(2);// up
			} 
			/*
			else if (y >= 3.9) {
				sendDirection(3);// down
			}
			*/ 
			else
				sendDirection(-1);
		}
	}
	
    @Override
	public void onAccuracyChanged(Sensor sensor, int accuracy) {
		// TODO Auto-generated method stub		
	}
	
    public void onToggleClicked(View view) {
    	if (tbTilt.isChecked()){	
			senAccelerometer = senSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
			senSensorManager.registerListener(this, senAccelerometer,SensorManager.SENSOR_DELAY_UI);
			this.onResume();	
		}
    	else{
    		tiltDirection.setText("");
    		this.onPause();
    	}			
	}
    
 	public void sendDirection(int direction) {
 		if (direction == 0) {
 			tiltDirection.setText("Left");

			if (myBTservice.getState() == myBTservice.STATE_CONNECTED) {
				switch (robot.getDirection()) {
					case UP:
						sendMessage("Left");		
						break;
						
					case LEFT:
						sendMessage("Down");
						break;
						
					case DOWN:
						sendMessage("Right");
						break;
						
					case RIGHT:
						sendMessage("Up");
						break;
				}
			}
			robot.rotateLeft();
			draw.refreshPuzzle();
		} 
 		else if (direction == 1) {
			tiltDirection.setText("Right");

			if (myBTservice.getState() == myBTservice.STATE_CONNECTED) {
				switch (robot.getDirection()) {
					case UP:
						sendMessage("Right");
						break;
				
					case LEFT:
						sendMessage("Up");
						break;
				
					case DOWN:
						sendMessage("Left");
						break;
					
					case RIGHT:
						sendMessage("Down");
						break;
				}
			}
			robot.rotateRight();
			draw.refreshPuzzle();
		}
		else if (direction == 2) {
			tiltDirection.setText("Up");

			if (myBTservice.getState() == myBTservice.STATE_CONNECTED) {
				switch (robot.getDirection()) {
					case UP:
						sendMessage("Up");
						break;
						
					case DOWN:
						sendMessage("Down");
						break;
						
					case LEFT:
						sendMessage("Left");
						break;
						
					case RIGHT:
						sendMessage("Right");
						break;
				}
			}
			robot.moveForward();
			draw.refreshPuzzle();
		} 
		else if (direction == 3) {
			tiltDirection.setText("Down");

			// switch (robot.getDirection()) {
			// case UP:
			// sendMessage("s");
			// break;
			// case DOWN:
			// sendMessage("w");
			// break;
			// case LEFT:
			// sendMessage("d");
			// break;
			// case RIGHT:
			// sendMessage("a");
			// break;
			// }
			// robot.rotateHalfCircle();
			// draw.refreshPuzzle();

		} 
		else {			
			tiltDirection.setText("Stop");
		}

		// draw.refreshPuzzle();
		// try {
		// Thread.sleep(1000);
		// } catch (Exception e) {
		//
		// }

 	}
    
 	//methods across Task C.3 - C.5
	@Override
	public boolean onTouch(View v, MotionEvent event) {
    	String map;
		map = draw.getCurrentMap();
    	
    	if (event.getAction() == MotionEvent.ACTION_DOWN) {
			switch (v.getId()) {
				case R.id.btnForward:
					up = true;
					mdHandler = new Handler();
					mdHandler.postDelayed(mAction, 10);
					break;

				/*
				case R.id.btn_down:
					down = true;
					mdHandler = new Handler();
					mdHandler.postDelayed(mAction, 1000);
					break;
				*/
					
				case R.id.btnRotateLeft:
					left = true;
					mdHandler = new Handler();
					mdHandler.postDelayed(mAction, 10);
					break;

				case R.id.btnRotateRight:
					right = true;
					mdHandler = new Handler();    
					mdHandler.postDelayed(mAction, 10);
					break;
					
				default:	
					break;
			}
		} 
    	else if (event.getAction() == MotionEvent.ACTION_UP) {
			switch (v.getId()) {
				case R.id.btnForward:
					up = false;
					mdHandler.removeCallbacks(mAction);
					mdHandler = null;
					
					//detect if robot stop moving, via release of click
					robotStatus.setText("Robot Stopped Moving");
					break;
				
				/*
				case R.id.btn_down:
					down = false;
					mdHandler.removeCallbacks(mAction);
					mdHandler = null;
					break;
				*/
			
				case R.id.btnRotateLeft:
					left = false;
					mdHandler.removeCallbacks(mAction);
					mdHandler = null;
					
					robotStatus.setText("Robot Stopped");
					break;
					
				case R.id.btnRotateRight:
					right = false;
					mdHandler.removeCallbacks(mAction);
					mdHandler = null;		
					
					robotStatus.setText("Robot Stopped");					
					break;
					
				default:
					break;
			}
			// sendMessage(map);
		}
		return true;
    }
           
    Runnable mAction = new Runnable() {
		@Override
		public void run() {
			//robot speed
			mdHandler.postDelayed(this, 100);
			Draw draw = (Draw) findViewById(R.id.map);
			if (up) {
				// Toast.makeText(getApplicationContext(), "up",
				// Toast.LENGTH_SHORT).show();
				System.out.println("up");			

				switch (robot.getDirection()) {
					case UP:
						sendMessage("Up");
						robotStatus.setText("Facing Up");
						break;
						
					case DOWN:
						sendMessage("Down");
						robotStatus.setText("Facing Down");
						break;
						
					case LEFT:
						sendMessage("Left");
						robotStatus.setText("Facing Left");
						break;
						
					case RIGHT:
						sendMessage("Right");
						robotStatus.setText("Facing Right");
						break;
				}				
				robot.moveForward();
				draw.refreshPuzzle();

				System.out.println("location" + robot.getX() + robot.getY());
			} 
			/*
			else if (down) {
				// Toast.makeText(getApplicationContext(), "down",
				// Toast.LENGTH_SHORT).show();
				System.out.println("down");

				robot.rotateHalfCircle();
				draw.refreshPuzzle();

				System.out.println("location" + robot.getX() + robot.getY());

			}*/			
			else if (left) {
				// Toast.makeText(getApplicationContext(), "left",
				// Toast.LENGTH_SHORT).show();
				System.out.println("left");
				
				switch (robot.getDirection()) {
					case UP:
						sendMessage("Left");
						robotStatus.setText("Facing Left");
						break;
						
					case LEFT:
						sendMessage("Down");
						robotStatus.setText("Facing Down");
						break;
						
					case DOWN:
						sendMessage("Right");
						robotStatus.setText("Facing Right");
						break;
						
					case RIGHT:
						sendMessage("Up");
						robotStatus.setText("Facing Up");
						break;
				}				
				robot.rotateLeft();
				draw.refreshPuzzle();

				System.out.println("location" + robot.getX() + robot.getY());

			} 
			else if (right) {
				// Toast.makeText(getApplicationContext(), "right",
				// Toast.LENGTH_SHORT).show();
				System.out.println("right");
				
				switch (robot.getDirection()) {
					case UP:
						sendMessage("Right");
						robotStatus.setText("Facing Right");
						break;
						
					case LEFT:
						sendMessage("Up");
						robotStatus.setText("Facing Up");
						break;
						
					case DOWN:
						sendMessage("Left");
						robotStatus.setText("Facing Left");
						break;
						
					case RIGHT:
						sendMessage("Down");
						robotStatus.setText("Facing Down");
						break;
				}
				robot.rotateRight();
				draw.refreshPuzzle();

				System.out.println("location" + robot.getX() + robot.getY());

			} 
			else {
				// Toast.makeText(getApplicationContext(), "null",
				// Toast.LENGTH_SHORT).show();
				System.out.println("null");
			}
			System.out.println("++location: " + robot.getX() + robot.getY());
		}
	};
	
	public void onToggleAutoManual(View view) {
		boolean auto = tbAutoManual.isChecked();

		if (auto) {
			btnUpdateMap.setEnabled(false);
			Toast.makeText(getApplicationContext(), "Auto enabled!", Toast.LENGTH_SHORT).show();

			// new onAuto(view, this).execute(newPuzzle);
		} 
		else {
			btnUpdateMap.setEnabled(true);
			Toast.makeText(getApplicationContext(), "Auto disabled!", Toast.LENGTH_SHORT).show();
		}
	}

	public void getMapData(View view) {
		draw.getCurrentMap();
	}
	
	//methods to Task C.7
	public void sendStoredStrings1() {
		StoredString1 = preferences.getString("key_msg1", "na");
		//Toast.makeText(getApplicationContext(), StoredString1, Toast.LENGTH_SHORT).show();
		sendMessage(StoredString1);
	}

	public void sendStoredStrings2() {
		StoredString2 = preferences.getString("key_msg2", "na");
		//Toast.makeText(getApplicationContext(), StoredString2, Toast.LENGTH_SHORT).show();
		sendMessage(StoredString2);
	}
	
	public void sendStoredStrings3() {
		StoredString3 = preferences.getString("key_msg3", "na");
		sendMessage(StoredString3);
	}
	
	public void sendStoredStrings4() {
		StoredString4 = preferences.getString("key_msg4", "na");
		sendMessage(StoredString4);
	}
			
	//methods across Task C.1, C.2, C.9
	public void onResume() {
		super.onResume();	

		senSensorManager.registerListener(this, senAccelerometer, SensorManager.SENSOR_DELAY_UI);
		this.tbTilt.setChecked(true);

        if(D) Log.e(TAG, "+ ON RESUME +");
        
        // onResume() called when ACTION_REQUEST_ENABLE activity returns.
        if (myBTservice != null) {
            if (myBTservice.getState() == myBTservice.STATE_NONE) {
            	myBTservice.start();
            }
        }
    }	
	
	@Override
	public void onDestroy() {
		super.onDestroy();
		
		senSensorManager.unregisterListener(this);
		
		if (myBTservice != null) 
			myBTservice.stop();
        
		if(D) 
        	Log.e(TAG, "--- ON DESTROY ---");
	}
	
	@Override
	public void onPause(){
		super.onPause();
		
		senSensorManager.unregisterListener(this);
	}
}//end class