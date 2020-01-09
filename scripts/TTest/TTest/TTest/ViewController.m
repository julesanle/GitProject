//
//  ViewController.m
//  TTest
//
//  Created by LiuWenXing on 2018/6/21.
//  Copyright © 2018年 WnirVana. All rights reserved.
//

#import "ViewController.h"
#import "zlib.h"

@interface ViewController ()
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    NSData *data = [self uncompressZippedData:[self dencode:@"H4sIAAAAAAAAE31STWsUQRD9L509zi7d871zW/MBi6DCCh5Eht6ZmkybmemhuychhJz04CHx5EUUQZB4yR48CEEQ/8wu0X9h9exGDH704UFXV73XVfUenxAjaiAJC7xxGFI3pmMaOiQ1imcHqchJ4sYho9SndOwQOITGkIQMJm07M1wZgqlF1eky/YPGow7JhTaiyUxPRBiyxKEb+S5lfsCiIIyxvlWyBWUEaJKckIHOFECTHonclCTxmd9nPIXM6hrISiwZ8LZND0FpIRvLO2IjasNCp4VQ2qQ5PyZJwSsNGK1lDhWmiQelbIBRx8Vc3c03nIxR10HwLPgWAguhhchCbGGMgKURfj0KnSGzcjkcigzWvXl+EHkRC4e7uyEb+nseHU6infFwO4jvhLE/2Q5CKzvIuFICFFYsrxarN1+vX31efntvXxowR1IdpOa4xUGSR9O9qf2n4fv2ylzq4fUvTR+JQpDEqA571VkpZXWP21WQ1fnL5dXb1dWL72fPVh8+rhYX15eXyy9nP14/X316Z+UXF5ZAge5qSAsl63SOW99XsmvyX/NrK24KqWpknN6fkRuR6Q4GXGpP39hmbyWI/RLHGnnookEl5rf3REcstNlS/x53Rxgn63y7qF5mUPOmK3hmOtXPCy1XAcY7DUrJynbo3Vr62oE3W5d6w3TqkM1Ie09jSa9ysv5dDoYL644ZNFoqPWl4dWxEpmc7d7e2oOHzCiadkQ9tbbKFh/yvr1sN/MOltrgGU0rrmwzNSU5Pn/wExQcHF4kDAAA="]];
    NSString *string = [[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];
    NSLog(@"%@", string);
}

- (NSData *)dencode:(NSString *)base64String {
    NSData *data = [[NSData alloc]initWithBase64EncodedString:base64String options:NSDataBase64DecodingIgnoreUnknownCharacters];
    return data;
}

-(NSData *)uncompressZippedData:(NSData *)compressedData
{
    if ([compressedData length] == 0) return compressedData;
    
    unsigned full_length = [compressedData length];
    
    unsigned half_length = [compressedData length] / 2;
    NSMutableData *decompressed = [NSMutableData dataWithLength: full_length + half_length];
    BOOL done = NO;
    int status;
    z_stream strm;
    strm.next_in = (Bytef *)[compressedData bytes];
    strm.avail_in = [compressedData length];
    strm.total_out = 0;
    strm.zalloc = Z_NULL;
    strm.zfree = Z_NULL;
    if (inflateInit2(&strm, (15+32)) != Z_OK) return nil;
    while (!done) {
        // Make sure we have enough room and reset the lengths.
        if (strm.total_out >= [decompressed length]) {
            [decompressed increaseLengthBy: half_length];
        }
        // chadeltu 加了(Bytef *)
        strm.next_out = (Bytef *)[decompressed mutableBytes] + strm.total_out;
        strm.avail_out = [decompressed length] - strm.total_out;
        // Inflate another chunk.
        status = inflate (&strm, Z_SYNC_FLUSH);
        if (status == Z_STREAM_END) {
            done = YES;
        } else if (status != Z_OK) {
            break;
        }
        
    }
    if (inflateEnd (&strm) != Z_OK) return nil;
    // Set real length.
    if (done) {
        [decompressed setLength: strm.total_out];
        return [NSData dataWithData: decompressed];
    } else {
        return nil;
    }
}

@end
