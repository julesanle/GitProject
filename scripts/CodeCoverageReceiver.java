package com.yanxiu.yxtrain_android.test;


import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * Created by admin on 2017/6/2.
 */

public class CodeCoverageReceiver extends BroadcastReceiver {
    public static String TAG = "CodeCoverageReceiver:";
    private static String DEFAULT_COVERAGE_FILE_PATH = "/mnt/sdcard/coverage.ec";

    @Override
    public void onReceive(Context context, Intent intent) {
        generateCoverageReport();
    }

    private void generateCoverageReport() {
        Log.d(TAG, "generateCoverageReport():" + DEFAULT_COVERAGE_FILE_PATH);
        OutputStream out = null;
        try {
            java.io.File coverageDir = new java.io.File("/mnt/sdcard/coverage/"); //这里是写入覆盖率工具的 sd 卡上的目录
            if(!coverageDir.exists()){
                coverageDir.mkdirs();
            }
            java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("yyyyMMddHHmmssSSS");
            String coverageFileName = sdf.format(new java.util.Date())+".ec";
            java.io.File file = new java.io.File(coverageDir,coverageFileName);
            out = new FileOutputStream(file, false);
            Object agent = Class.forName("org.jacoco.agent.rt.RT")
                    .getMethod("getAgent")
                    .invoke(null);
            out.write((byte[]) agent.getClass().getMethod("getExecutionData", boolean.class)
                    .invoke(agent, false));
        } catch (Exception e) {
            Log.d(TAG, e.toString(), e);
        } finally {
            if (out != null) {
                try {
                    out.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
