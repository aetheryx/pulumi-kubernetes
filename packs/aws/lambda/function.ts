// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class Function extends lumi.NamedResource implements FunctionArgs {
    public readonly arn?: string;
    public readonly deadLetterConfig?: { targetArn: string }[];
    public readonly description?: string;
    public readonly environment?: { variables?: {[key: string]: string} }[];
    public readonly filename?: string;
    public readonly functionName: string;
    public readonly handler: string;
    public readonly invokeArn?: string;
    public readonly kmsKeyArn?: string;
    public readonly lastModified?: string;
    public readonly memorySize?: number;
    public readonly publish?: boolean;
    public readonly qualifiedArn?: string;
    public readonly role: string;
    public readonly runtime: string;
    public readonly s3Bucket?: string;
    public readonly s3Key?: string;
    public readonly s3ObjectVersion?: string;
    public readonly sourceCodeHash?: string;
    public readonly tags?: {[key: string]: any};
    public readonly timeout?: number;
    public readonly tracingConfig?: { mode: string }[];
    public readonly version?: string;
    public readonly vpcConfig?: { securityGroupIds: string[], subnetIds: string[], vpcId?: string }[];

    constructor(name: string, args: FunctionArgs) {
        super(name);
        this.arn = args.arn;
        this.deadLetterConfig = args.deadLetterConfig;
        this.description = args.description;
        this.environment = args.environment;
        this.filename = args.filename;
        this.functionName = args.functionName;
        this.handler = args.handler;
        this.invokeArn = args.invokeArn;
        this.kmsKeyArn = args.kmsKeyArn;
        this.lastModified = args.lastModified;
        this.memorySize = args.memorySize;
        this.publish = args.publish;
        this.qualifiedArn = args.qualifiedArn;
        this.role = args.role;
        this.runtime = args.runtime;
        this.s3Bucket = args.s3Bucket;
        this.s3Key = args.s3Key;
        this.s3ObjectVersion = args.s3ObjectVersion;
        this.sourceCodeHash = args.sourceCodeHash;
        this.tags = args.tags;
        this.timeout = args.timeout;
        this.tracingConfig = args.tracingConfig;
        this.version = args.version;
        this.vpcConfig = args.vpcConfig;
    }
}

export interface FunctionArgs {
    readonly arn?: string;
    readonly deadLetterConfig?: { targetArn: string }[];
    readonly description?: string;
    readonly environment?: { variables?: {[key: string]: string} }[];
    readonly filename?: string;
    readonly functionName: string;
    readonly handler: string;
    readonly invokeArn?: string;
    readonly kmsKeyArn?: string;
    readonly lastModified?: string;
    readonly memorySize?: number;
    readonly publish?: boolean;
    readonly qualifiedArn?: string;
    readonly role: string;
    readonly runtime: string;
    readonly s3Bucket?: string;
    readonly s3Key?: string;
    readonly s3ObjectVersion?: string;
    readonly sourceCodeHash?: string;
    readonly tags?: {[key: string]: any};
    readonly timeout?: number;
    readonly tracingConfig?: { mode: string }[];
    readonly version?: string;
    readonly vpcConfig?: { securityGroupIds: string[], subnetIds: string[], vpcId?: string }[];
}
