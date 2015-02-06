package model;

import entity.Cell;
import observer.RobotObserver;

public class Robot {
	private static final Robot robot = new Robot();
	public static final int SIZE = 3;
	    
	public static final int UP = 0;
	public static final int RIGHT = 1;
	public static final int DOWN = 2;
	public static final int LEFT = 3;
	  
	public static final int dx[] = {0, 1, 0, -1};
	public static final int dy[] = {-1, 0 , 1, 0};
	    
	private int x;
	private int y;
	private int direction;
	   
	public Robot() {
		direction = DOWN;
	    this.x = 8;  
	    this.y = 6;
	}
	    
	public static Robot getInstance() {
		return robot;
	}
	 
	public int getX() {
		return x;
	}
	 
	public void setX(int x) {
		this.x = x;
	    RobotObserver.getInstance().noticeView();
	}
	 
	public int getY() {
		return y;
	}	 
	
	public void setY(int y) {
		this.y = y;
		RobotObserver.getInstance().noticeView();
	}
	 
	public int getDirection() {
		return direction;
	}
	 
	public void setDirection(int direction) {
		this.direction = direction;
	}
	    
	public void rotateRight() {	
		//System.out.println("Rebote inside class X: "+this.x+" Y: "+this.y);
		direction = (direction + 1) % 4;
	    RobotObserver.getInstance().noticeView();
	}
	    
	   public void rotateLeft() {
	       //System.out.println("Rebote inside class X: "+this.x+" Y: "+this.y);
	       direction = (direction - 1 + 4) % 4;
	       RobotObserver.getInstance().noticeView();
	   }
	    
	   public void rotateHalfCircle(){
	       direction = (direction - 2 + 4) % 4;
	       RobotObserver.getInstance().noticeView();
	   }
	    
	   public void moveForward() {
	       //System.out.println("Rebote inside class X: "+this.x+" Y: "+this.y);
	       moveForward(1);
	   }
	    
	   public void moveForward(int numberOfMove) {
	       //System.out.println("Rebote inside class X: "+this.x+" Y: "+this.y);
	       int newX = x + dx[direction] * numberOfMove;
	       int newY = y + dy[direction] * numberOfMove;
	        
	       boolean check = true;
	       for (int i = 0; i < SIZE; i++)
	           for (int j = 0; j < SIZE; j++) {
	               if (!Arena.getInstance().insideArena(new Cell(newX + i, newY +j)))
	                   check = false;
	           }
	        
	       if (check) {
	           this.setX(newX);
	           this.setY(newY);
	           RobotObserver.getInstance().noticeView();
	       }
	   }
}
