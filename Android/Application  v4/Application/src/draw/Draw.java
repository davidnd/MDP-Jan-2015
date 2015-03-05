package draw;

import model.Arena;
import model.Robot;
import com.example.application.TaskC1;

import entity.Cell;

import android.R;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Paint.Style;
import android.graphics.Rect;
import android.graphics.RectF;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;

public class Draw extends View {
    private static final String TAG = "MDP";
    private TaskC1 game;
    public Robot robot;
 
    private float width;
    private float finalWidth;
    private float height;
    private int selX;
    private int selY;
    private final Rect selRect = new Rect();
    public String easyPuzzle = "";
    Canvas canvas;
    String finalPuzzle;
    int gridX, gridY;
    public int puzzle[] = new int[gridX * gridY];
    public static final int UP = 0;
    public static final int RIGHT = 1;
    public static final int DOWN = 2;
    public static final int LEFT = 3;
 
    public Draw(Context context, AttributeSet attrs) {
        super(context, attrs);
 
        Log.d("puzzleview", "working!");
        this.game = (TaskC1) game;
        this.robot = new Robot();
 
        setFocusable(true);
        setFocusableInTouchMode(true);
    }
 
    public void setPuzzle(String setPuzzle) {
        String[] puzzlearray;
        String finalPuzzleString;
 
        this.easyPuzzle = setPuzzle;
 
        Log.e("setPuzzle", setPuzzle);
 
        puzzlearray = setPuzzle.split(" ");
 
        gridY = 15;
        gridX = 20;

        robot.setX(Integer.parseInt(puzzlearray[0]));
        robot.setY(Integer.parseInt(puzzlearray[1]));
        robot.setDirection(Integer.parseInt(puzzlearray[2]));
 
        finalPuzzleString = puzzlearray[3];
 
        Log.i("finalPuzzleTHIS ONE", finalPuzzleString);
 
        finalPuzzle = finalPuzzleString;
 
        Log.i("draw", "suceed?" + finalPuzzle);
 
        this.puzzle = getPuzzle(finalPuzzle);
        this.refreshPuzzle();
        adjustWidth(gridX);
    }
 
    public void refreshPuzzle() {
        this.puzzle = getPuzzle(finalPuzzle);
        invalidate();
    }
 
    private int[] getPuzzle(String finalPuzzle) {
        return fromPuzzleString(finalPuzzle);
    }
 
    // use a long string to store the 9*9 = 81 numbers
    // the function is to convert all 81 numbers from the string
    static protected int[] fromPuzzleString(String string) {
        int[] puz = new int[string.length()];
        Log.i("draw", "str leng" + string.length() + "");
        for (int i = 0; i < puz.length; i++){
        	// get the number one digit by another        
            puz[i] = string.charAt(i) - '0';
        }
        return puz;
    }
 
    protected void onSizeChanged(int w, int h, int oldw, int oldh) { 
        width = (float) w / 25;
        height = width;
        finalWidth = width;
        getRect(selX, selY, selRect);
        Log.d(TAG, "onSizeChanged:width " + width + ",height " + height);
 
        adjustWidth(gridX);
        super.onSizeChanged(w, h, oldw, oldh);
        
    }
 
    protected void adjustWidth(int numberOfGrid) {
        width = finalWidth * 20 / numberOfGrid;
        height = width;
    }
 
    private void getRect(int x, int y, Rect rect) {
        rect.set((int) (x * width), (int) (y * height), (int) (x * width + width), (int) (y * height + height));
    }
 
    @Override
    protected void onDraw(Canvas canvas) {
        // draw the background
        Log.d("painting", "one time");
 
        drawArena(canvas);
        drawRobot(canvas);
    }
 
    private void drawRobot(Canvas canvas) {
        Paint painter = new Paint();
        painter.setColor(getResources().getColor(R.color.black));
        painter.setStyle(Style.STROKE);
 
        ///int x = (int) (robot.getX() * width + 3 * width / 2);
        ///int y = (int) (robot.getY() * width + 3 * width / 2);
        
        int x = (int) (robot.getX() * width - width / 2);
        int y = (int) (robot.getY() * width - width / 2);
        
        canvas.drawCircle(x, y, width, painter); 
        painter.setStyle(Style.FILL);
        
        switch (robot.getDirection()) {
        	case Robot.UP:
        		canvas.drawRect(new RectF((float) x - (width / 4), y - (width / 2 + width / 4), (float) x + width / 4, y - (width / 2)), painter);
        		break;
        		
        	case Robot.DOWN:
        		canvas.drawRect(new RectF((float) x - width / 4, y + (width / 2), (float) x + width / 4, y + (width / 2 + width / 4)), painter);
        		break;
        
        	case Robot.LEFT:
        		canvas.drawRect(new RectF((float) x - (width / 2 + width / 4), y - width / 4, (float) x - (width / 2), y + width / 4), painter);
        		break;
        			
        	case Robot.RIGHT:
        		canvas.drawRect(new RectF((float) x + (width / 2), y - width / 4, (float) x + (width / 2 + width / 4), y + width / 4), painter);
        		break;
        }
        Log.d("painting", "paint robot");
    }
 
    private void drawArena(Canvas canvas) {
        Paint painter = new Paint();
        painter.setColor(getResources().getColor(R.color.black));
       
        Paint painterUn = new Paint();
        painterUn.setColor(getResources().getColor(R.color.holo_blue_light));
        painterUn.setStyle(Style.FILL);
        
        // Horizontal lines
        for (int i = 0; i <= gridY; i++) {
            //canvas.drawLine(0, i * height, getWidth(), i * height, painter);
            canvas.drawLine(0, i * height, gridX * width, i * height, painter);
        }
        
        // Vertical lines
        for (int i = 0; i <= gridX; i++) {
            canvas.drawLine(i * width, 0, i * width, gridY * height, painter);
        }
        
        
        
        // blocks - vertical @ outer loop, horizontal @ inner loop
        painter.setStyle(Style.FILL);
        for (int y = 1; y <= gridY; y++) 
        {
            for (int x = 1; x <= gridX; x++)
            {
            	/*
            	if (this.getTileString(x, y) == 0)
            	{
            		Arena.getInstance().addEmptyCell(new Cell(x, y));
            	}
            	*/
            	
            	if (this.getTileString(x, y) == 1) // 1: block, 0:empty
                {
                    // Log.i("draw","grid@"+i+" "+j);
                    canvas.drawRect(new RectF((x-1) * width, (y-1) * height, x * width, y * height), painter);
                    //Arena.getInstance().addObstacleCell(new Cell(x, y));
                    //Arena.puzzle=this.puzzle;
                }
                
                else if(this.getTileString(x, y) == 2){
                	canvas.drawRect(new RectF((x-1) * width, (y-1) * height, x * width, y * height), painterUn);
                }
            }
        }
        Arena.puzzle=this.puzzle;
 
        // print start and end point
        Paint painter1 = new Paint();
        painter1.setColor(getResources().getColor(R.color.holo_red_light));
        painter1.setStyle(Style.FILL);
        canvas.drawRect(new RectF(0 * width, 0 * height, 3 * width, 3 * height), painter1);
        canvas.drawRect(new RectF((gridX - 3) * width, (gridY - 3) * height, gridX * width, gridY * height), painter1);
 
        Log.d("painting", "paint arena");
    }
 
    public int getTileString(int x, int y) {
        Log.i("draw", "at here" + x + " " + y);
        int v = getTile(x, y);
        
        return v;
        
    }
 
    private int getTile(int x, int y) { 
   
        //return this.puzzle[y * gridX + x];
        return this.puzzle[(y-1) * gridX + (x-1)];
    }
 
    public String getCurrentMap() {
        String map = "GRID";
        Log.i("setPuzzle", easyPuzzle);
        String puzzlearray[];
        String obsPuzzle = "";
 
        // get arena size
        map += " " + this.gridY;
        map += " " + this.gridX;
 
        // get robot position
        map += " " + String.valueOf(robot.getX() + 1);
        map += " " + String.valueOf(robot.getY() + 1);
 
        // get robot direction
        switch (robot.getDirection()) {
        	case UP:
        		map += " " + String.valueOf(robot.getX() + 1);
        		
        		if (robot.getY() - 1 >= 0)
        			map += " " + String.valueOf(robot.getY() - 1 + 1);
        		else
        			map += " " + "0";
        		break;
        		
        	case DOWN:
        		map += " " + String.valueOf(robot.getX() + 1);
        		map += " " + String.valueOf(robot.getY() + 1 + 1);
        		break;
        		
        	case LEFT:
        		if (robot.getX() - 1 >= 0)
        			map += " " + String.valueOf(robot.getX() - 1 + 1);
        		else
        			map += " " + "0";
        		map += " " + String.valueOf(robot.getY() + 1);
        		break;
        
        	case RIGHT:
        		map += " " + String.valueOf(robot.getX() + 1 + 1);
        		map += " " + String.valueOf(robot.getY() + 1);
        		break;
        }
 
        // get obstacles
        puzzlearray = easyPuzzle.split(" ");
        
        for (int i = 7; i < puzzlearray.length; i++)
            obsPuzzle = obsPuzzle + puzzlearray[i]; 
       
        map += " " + obsPuzzle.replace("", " ").trim();         
        Log.i("mapGETDATA", map); 
        return map;
    }
}
