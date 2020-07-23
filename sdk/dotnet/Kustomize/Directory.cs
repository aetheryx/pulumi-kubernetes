// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using Pulumi.Kubernetes.Yaml;

namespace Pulumi.Kubernetes.Kustomize
{
    /// <summary>
    /// Directory is a component representing a collection of resources described by a kustomize directory (kustomization).
    /// 
    /// ## Example Usage
    /// ### Local Kustomize Directory
    /// 
    /// ```csharp
    /// using System.Threading.Tasks;
    /// using Pulumi;
    /// using Pulumi.Kubernetes.Kustomize;
    /// 
    /// class KustomizeStack : Stack
    /// {
    ///     public KustomizeStack()
    ///     {
    ///         var helloWorld = new Directory("helloWorldLocal", new DirectoryArgs
    ///         {
    ///             Directory = "./helloWorld",
    ///         });
    ///     }
    /// }
    /// ```
    /// ### Kustomize Directory from a Git Repo
    /// 
    /// ```csharp
    /// using System.Threading.Tasks;
    /// using Pulumi;
    /// using Pulumi.Kubernetes.Kustomize;
    /// 
    /// class KustomizeStack : Stack
    /// {
    ///     public KustomizeStack()
    ///     {
    ///         var helloWorld = new Directory("helloWorldRemote", new DirectoryArgs
    ///         {
    ///             Directory = "https://github.com/kubernetes-sigs/kustomize/tree/v3.3.1/examples/helloWorld",
    ///         });
    ///     }
    /// }
    /// ```
    /// ### Kustomize Directory with Transformations
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Collections.Immutable;
    /// using System.Threading.Tasks;
    /// using Pulumi;
    /// using Pulumi.Kubernetes.Kustomize;
    /// 
    /// class KustomizeStack : Stack
    /// {
    ///     public KustomizeStack()
    ///     {
    ///         var helloWorld = new Directory("helloWorldRemote", new DirectoryArgs
    ///         {
    ///             Directory = "https://github.com/kubernetes-sigs/kustomize/tree/v3.3.1/examples/helloWorld",
    ///             Transformations =
    ///               {
    ///                   LoadBalancerToClusterIP,
    ///                   ResourceAlias,
    ///                   OmitTestPod,
    ///               }
    ///         });
    /// 
    ///         // Make every service private to the cluster, i.e., turn all services into ClusterIP instead of LoadBalancer.
    ///         ImmutableDictionary&lt;string, object&gt; LoadBalancerToClusterIP(ImmutableDictionary&lt;string, object&gt; obj, CustomResourceOptions opts)
    ///         {
    ///             if ((string)obj["kind"] == "Service" &amp;&amp; (string)obj["apiVersion"] == "v1")
    ///             {
    ///                 var spec = (ImmutableDictionary&lt;string, object&gt;)obj["spec"];
    ///                 if (spec != null &amp;&amp; (string)spec["type"] == "LoadBalancer")
    ///                 {
    ///                     return obj.SetItem("spec", spec.SetItem("type", "ClusterIP"));
    ///                 }
    ///             }
    /// 
    ///             return obj;
    ///         }
    /// 
    ///         // Set a resource alias for a previous name.
    ///         ImmutableDictionary&lt;string, object&gt; ResourceAlias(ImmutableDictionary&lt;string, object&gt; obj, CustomResourceOptions opts)
    ///         {
    ///             if ((string)obj["kind"] == "Deployment")
    ///             {
    ///                 opts.Aliases = new List&lt;Input&lt;Alias&gt;&gt; { new Alias { Name = "oldName" } };
    ///             }
    /// 
    ///             return obj;
    ///         }
    /// 
    ///         // Omit a resource from the Chart by transforming the specified resource definition to an empty List.
    ///         ImmutableDictionary&lt;string, object&gt; OmitTestPod(ImmutableDictionary&lt;string, object&gt; obj, CustomResourceOptions opts)
    ///         {
    ///             var metadata = (ImmutableDictionary&lt;string, object&gt;)obj["metadata"];
    ///             if ((string)obj["kind"] == "Pod" &amp;&amp; (string)metadata["name"] == "test")
    ///             {
    ///                 return new Dictionary&lt;string, object&gt;
    ///                 {
    ///                     ["apiVersion"] = "v1",
    ///                     ["kind"] = "List",
    ///                     ["items"] = new Dictionary&lt;string, object&gt;(),
    ///                 }.ToImmutableDictionary();
    ///             }
    /// 
    ///             return obj;
    ///         }
    ///     }
    /// }
    /// ```
    /// </summary>
    public sealed class Directory : CollectionComponentResource
    {
        /// <summary>
        /// Create a Directory resource with the given unique name, arguments, and options.
        /// </summary>
        /// <param name="name">Name of the kustomization (e.g., nginx-ingress).</param>
        /// <param name="args">Configuration options for the kustomization.</param>
        /// <param name="options">Resource options.</param>
        public Directory(string name, DirectoryArgs args, ComponentResourceOptions? options = null)
            : base("kubernetes:kustomize:Directory", MakeName(args, name), options)
        {
            name = GetName(args, name);
            var objs = Invokes.KustomizeDirectory(new KustomizeDirectoryArgs { Directory = args.Directory });
            var configGroupArgs = new ConfigGroupArgs
            {
                ResourcePrefix = args.ResourcePrefix,
                Objs = objs,
                Transformations = args.Transformations
            };
            var opts = ComponentResourceOptions.Merge(options, new ComponentResourceOptions { Parent = this });
            var resources = Parser.Parse(configGroupArgs, opts);
            RegisterResources(resources);
        }
        private static string MakeName(DirectoryArgs? args, string name)
            => args?.ResourcePrefix != null ? $"{args.ResourcePrefix}-{name}" : name;

        private static string GetName(DirectoryArgs config, string releaseName)
        {
            var prefix = config.ResourcePrefix;
            return string.IsNullOrEmpty(prefix) ? releaseName : $"{prefix}-{releaseName}";
        }

    }

    /// <summary>
    /// Resource arguments for <see cref="Directory"/>.
    /// </summary>
    public class DirectoryArgs : ResourceArgs
    {
        /// <summary>
        /// The directory containing the kustomization to apply. The value can be a local directory or a folder in a
        /// git repository.
        /// Example: ./helloWorld
        /// Example: https://github.com/kubernetes-sigs/kustomize/tree/master/examples/helloWorld
        /// </summary>
        public string? Directory { get; set; }

        private List<TransformationAction>? _transformations;

        /// <summary>
        /// Optional array of transformations to apply to resources that will be created by this chart prior to
        /// creation. Allows customization of the chart behaviour without directly modifying the chart itself.
        /// </summary>
        public List<TransformationAction> Transformations
        {
            get => _transformations ??= new List<TransformationAction>();
            set => _transformations = value;
        }

        /// <summary>
        /// An optional prefix for the auto-generated resource names.
        /// Example: A resource created with resourcePrefix="foo" would produce a resource named "foo-resourceName".
        /// </summary>
        public string? ResourcePrefix { get; set; }
    }
}
