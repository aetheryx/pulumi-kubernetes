// *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputApi from "../../types/input";
import * as outputApi from "../../types/output";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators"

    /**
     * DEPRECATED - This group version of Deployment is deprecated by apps/v1beta2/Deployment. See
     * the release notes for more information. Deployment enables declarative updates for Pods and
     * ReplicaSets.
     */
    export class Deployment extends pulumi.CustomResource {
      /**
       * APIVersion defines the versioned schema of this representation of an object. Servers should
       * convert recognized schemas to the latest internal value, and may reject unrecognized
       * values. More info:
       * https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
       */
      public readonly apiVersion: pulumi.Output<"extensions/v1beta1">;

      /**
       * Kind is a string value representing the REST resource this object represents. Servers may
       * infer this from the endpoint the client submits requests to. Cannot be updated. In
       * CamelCase. More info:
       * https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
       */
      public readonly kind: pulumi.Output<"Deployment">;

      /**
       * Standard object metadata.
       */
      public readonly metadata: pulumi.Output<outputApi.meta.v1.ObjectMeta>;

      /**
       * Specification of the desired behavior of the Deployment.
       */
      public readonly spec: pulumi.Output<outputApi.extensions.v1beta1.DeploymentSpec>;

      /**
       * Most recently observed status of the Deployment.
       */
      public readonly status: pulumi.Output<outputApi.extensions.v1beta1.DeploymentStatus>;

      /**
       * Get the state of an existing `Deployment` resource, as identified by `id`.
       * Typically this ID  is of the form <namespace>/<name>; if <namespace> is omitted, then (per
       * Kubernetes convention) the ID becomes default/<name>.
       *
       * Pulumi will keep track of this resource using `name` as the Pulumi ID.
       *
       * @param name _Unique_ name used to register this resource with Pulumi.
       * @param id An ID for the Kubernetes resource to retrieve. Takes the form
       *  <namespace>/<name> or <name>.
       * @param opts Uniquely specifies a CustomResource to select.
       */
      public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Deployment {
          return new Deployment(name, undefined, { ...opts, id: id });
      }

      public getInputs(): inputApi.extensions.v1beta1.Deployment { return this.__inputs; }
      private readonly __inputs: inputApi.extensions.v1beta1.Deployment;

      public static list(
        ctx: pulumi.query.ListContext,
        args?: pulumi.query.ListArgs,
      ): rxjs.Observable<outputApi.extensions.v1beta1.Deployment> {
        return ctx.list({...args, type: "kubernetes:extensions/v1beta1:Deployment",});
      }

      public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
          ...policy,
          pulumiType: "kubernetes:extensions/v1beta1:Deployment",
        });
      }

      /**
       * Create a extensions.v1beta1.Deployment resource with the given unique name, arguments, and options.
       *
       * @param name The _unique_ name of the resource.
       * @param args The arguments to use to populate this resource's properties.
       * @param opts A bag of options that control this resource's behavior.
       */
      constructor(name: string, args?: inputApi.extensions.v1beta1.Deployment, opts?: pulumi.CustomResourceOptions) {
          let inputs: pulumi.Inputs = {};
          inputs["apiVersion"] = "extensions/v1beta1";
          inputs["kind"] = "Deployment";
          inputs["metadata"] = args && args.metadata || undefined;
          inputs["spec"] = args && args.spec || undefined;
          inputs["status"] = args && args.status || undefined;
          super("kubernetes:extensions/v1beta1:Deployment", name, inputs, opts);
          this.__inputs = <any>args;
      }
    }